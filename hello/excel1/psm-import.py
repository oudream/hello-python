# pip install pandas xlrd

import sys, getopt
import pandas as pd
import sqlite3
import yaml
import re

'''
    step 1
    parse argv
'''

argv = sys.argv[1:]
excelFilePath = 'psm.xls'
dbFilePath = 'psm.db'
confFilePath = 'psm.yaml'
try:
    opts, args = getopt.getopt(argv, "he:d:", ["ef=", "df="])
except getopt.GetoptError:
    print('test.py -e <excel-file-path> -d <db-file-path>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('test.py -e <excel-file-path> -d <db-file-path>')
        sys.exit()
    elif opt in ("-e", "--ef"):
        excelFilePath = arg
    elif opt in ("-d", "--df"):
        dbFilePath = arg
    elif opt in ("-c", "--cf"):
        confFilePath = arg

'''
    step 2
    load excel file
'''

# use r before absolute file path
xls = pd.ExcelFile(excelFilePath)

# 2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis
sheetX = xls.parse("Sheet1")

'''
    step 3
    find title , index , count
'''

#
# *设备名称      f1
# *电压等级      f2
# 设备类型名称    f3
# 运行编号       f4
# *变电站名称     f5
# 间隔单元       f6
# 备注          f7
# *设备增加方式   f8
# 资产编号       f9
# 资产移交清册ID  fa

# col title
psmF1Title = '*设备名称'
psmF2Title = '*电压等级'
psmF3Title = '设备类型名称'
psmF4Title = '运行编号'
psmF5Title = '*变电站名称'
psmF6Title = '间隔单元'
psmF7Title = '备注'
psmF8Title = '*设备增加方式'
psmF9Title = '资产编号'
psmFaTitle = '资产移交清册ID'

# get col index
psmF1ColIndex = sheetX.columns.get_loc(psmF1Title)
psmF2ColIndex = sheetX.columns.get_loc(psmF2Title)
psmF3ColIndex = sheetX.columns.get_loc(psmF3Title)
psmF4ColIndex = sheetX.columns.get_loc(psmF4Title)
psmF5ColIndex = sheetX.columns.get_loc(psmF5Title)
psmF6ColIndex = sheetX.columns.get_loc(psmF6Title)
psmF7ColIndex = sheetX.columns.get_loc(psmF7Title)
psmF8ColIndex = sheetX.columns.get_loc(psmF8Title)
psmF9ColIndex = sheetX.columns.get_loc(psmF9Title)
psmFaColIndex = sheetX.columns.get_loc(psmFaTitle)

# get row count
psmRowCount = len(sheetX.index)
if psmRowCount > 100 * 1024:
    print("超出限制的行数")
    exit(-1)

print("输出列号："
      , psmF1ColIndex
      , psmF2ColIndex
      , psmF3ColIndex
      , psmF4ColIndex
      , psmF5ColIndex
      , psmF6ColIndex
      , psmF7ColIndex
      , psmF8ColIndex
      , psmF9ColIndex
      , psmFaColIndex
      )

'''
    step 4
    sql define
'''

psmSqlCreate = '''
CREATE TABLE `psm` (
  `fid` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `f1` TEXT DEFAULT '',
  `f2` TEXT DEFAULT '',
  `f3` TEXT DEFAULT '',
  `f4` TEXT DEFAULT '',
  `f5` TEXT DEFAULT '',
  `f6` TEXT DEFAULT '',
  `f7` TEXT DEFAULT '',
  `f8` TEXT DEFAULT '',
  `f9` TEXT DEFAULT '',
  `fa` TEXT DEFAULT '',
  `g1` TEXT DEFAULT '',
  `g2` TEXT DEFAULT '',
  `g3` TEXT DEFAULT '',
  `g4` TEXT DEFAULT '',
  `g5` TEXT DEFAULT ''
);
'''

psmSqlInsert = '''
INSERT INTO `psm`(`fid`, `f1`, `f2`, `f3`, `f4`, `f5`, `f6`, `f7`, `f8`, `f9`, `fa`, `g1`, `g2`, `g3`, `g4`, `g5`) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
'''

psmSqlUpdate = '''
UPDATE `psm` SET `f1` = ?, `f2` = ?, `f3` = ?, `f4` = ?, `f5` = ?, `f6` = ?, `f7` = ?, `f8` = ?, `f9` = ?, `fa` = ?, `g1` = ?, `g2` = ?, `g3` = ?, `g4` = ?, `g5` = ? WHERE `fid` = ?;
'''

psmSqlSelect = '''
SELECT `fid`, `f1`, `f2`, `f3`, `f4`, `f5`, `f6`, `f7`, `f8`, `f9`, `fa`, `g1`, `g2`, `g3`, `g4`, `g5`
FROM `psm`
'''

psmSqlDelete = '''DELETE FROM `psm`'''

con = sqlite3.connect(dbFilePath)


def isExistTable(cur, name):
    cur.execute("SELECT COUNT(*) AS COUNTER FROM `sqlite_master` WHERE `type`='table' AND `name`='{}';".format(name))
    # if the count is 1, then table exists
    if cur.fetchone()[0] == 1:
        return True
    else:
        return False


def psmConvertValue(v):
    if isinstance(v, str):
        return v
    else:
        return ''


try:
    cur = con.cursor()
    if not isExistTable(cur, 'psm'):
        cur.execute(psmSqlCreate)
    # commit
    con.commit()
    print("success - create table psm!")
except sqlite3.IntegrityError:
    con.rollback()
    print("ERROR - couldn't create table psm!")

'''
    step 5
    fetch
'''


# 0)、提取设备编号，（* 看文档-PMS台账功能.docx）
# 1)、提取电压等级，（从levels列表中按顺序匹配）
# 2)、提取间隔类型，
# 3)、提取设备类型，
# 4)、提取功能类型,


# 类定义
class MatchConditionItem:
    @staticmethod
    def Contain(src, sub):
        return sub in src

    @staticmethod
    def UnContain(src, sub):
        return not (sub in src)

    # 定义基本属性
    operation = ''
    content = ''
    func = Contain

    # 定义构造方法
    def __init__(self, o, c):
        self.operation = o
        self.content = c
        self.func = MatchConditionItem.Contain if o == '@' else MatchConditionItem.UnContain

    def match(self, src):
        return self.func(src, self.content)


# 类定义
class MatchCondition:
    # 定义基本属性
    value = ''
    ms = []

    # 定义构造方法
    def __init__(self, value, ms):
        self.value = value
        self.ms = []
        if ms is None:
            self.ms.append(MatchConditionItem('@', value))
        else:
            for m in ms:
                self.ms.append(MatchConditionItem(m['o'], m['c']))

    def match(self, src):
        for m in self.ms:
            if not m.match(src):
                return False
        return True


# 类定义
class MatchClass:
    # 定义基本属性
    name = ''
    vcs = []

    # 定义构造方法
    def __init__(self, name, vcs):
        self.name = name
        self.vcs = []
        for vc in vcs:
            self.vcs.append(MatchCondition(vc['v'], vc.get('ms')))

    def match_value(self, src):
        for vc in self.vcs:
            if vc.match(src):
                return vc.value
        return ""


noneMatch = MatchClass("", [])
levelMatch = noneMatch
bayMatch = noneMatch
deviceMatch = noneMatch

with open(confFilePath, encoding='utf-8') as file:
    data = yaml.safe_load(file)
    print(data)
    print(data['psm']['levels'])
    print(data['psm']['bays'])
    print(data['psm']['devices'])

    levelMatch = MatchClass("level", data['psm']['levels'])
    bayMatch = MatchClass("bay", data['psm']['bays'])
    deviceMatch = MatchClass("device", data['psm']['devices'])

    s1 = "2号主变110kV侧中性点2029接地隔离开关O相"
    r1 = levelMatch.match_value(s1)
    print("levelMatch 结果为：", r1)
    r1 = deviceMatch.match_value(s1)
    print("deviceMatch 结果为：", r1)

    print(str(data['psm']['bays']).split(','))


def fetchCode(src):
    ss = ["220kV", "110kV", "35kV", "10kV"]
    dest = src
    for s in ss:
        dest = dest.replace(s, '')
    res = r'([A-Za-z0-9]{2,})'
    mm = re.findall(res, dest, re.I)
    if len(mm) > 0:
        return mm[0]
    else:
        return ''


def indexSS(src, ss):
    idx = -1
    l = -1
    for s in ss:
        n = src.find(s)
        if n >= 0:
            if n < idx or idx == -1:
                idx = n
                l = len(s)
    return idx, l


def fetchFunc(src):
    b, bl = indexSS(src, ["=3", "=2", "=1", "="])
    if b < 0: return ""
    e, el = indexSS(src, [" ", ",", "，"])
    if e < 0: e = len(src)
    return src[b + bl:e]


try:
    cur = con.cursor()
    cur.execute(psmSqlDelete)
    psmDataSet = []
    for i in range(0, psmRowCount):
        # 0)、提取设备编号 from 设备名称 f1
        # 1)、提取电压等级 from 电压等级 f2
        # 2)、提取间隔类型 from 间隔单元 f6
        # 3)、提取设备类型 from 设备名称 f1
        # 4)、提取功能类型 from 备注    f7
        g1Value = fetchCode(psmConvertValue(sheetX.iat[i, psmF1ColIndex]))
        g2Value = levelMatch.match_value(psmConvertValue(sheetX.iat[i, psmF2ColIndex]))
        g3Value = bayMatch.match_value(psmConvertValue(sheetX.iat[i, psmF6ColIndex]))
        g4Value = deviceMatch.match_value(psmConvertValue(sheetX.iat[i, psmF1ColIndex]))
        g5Value = fetchFunc(psmConvertValue(sheetX.iat[i, psmF7ColIndex]))
        psmDataSet.append((psmConvertValue(sheetX.iat[i, psmF1ColIndex]),
                           psmConvertValue(sheetX.iat[i, psmF2ColIndex]),
                           psmConvertValue(sheetX.iat[i, psmF3ColIndex]),
                           psmConvertValue(sheetX.iat[i, psmF4ColIndex]),
                           psmConvertValue(sheetX.iat[i, psmF5ColIndex]),
                           psmConvertValue(sheetX.iat[i, psmF6ColIndex]),
                           psmConvertValue(sheetX.iat[i, psmF7ColIndex]),
                           psmConvertValue(sheetX.iat[i, psmF8ColIndex]),
                           psmConvertValue(sheetX.iat[i, psmF9ColIndex]),
                           psmConvertValue(sheetX.iat[i, psmFaColIndex]),
                           g1Value,
                           g2Value,
                           g3Value,
                           g4Value,
                           g5Value
                           ))
    cur.execute(psmSqlDelete)
    cur.executemany(psmSqlInsert, psmDataSet)
    # commit
    con.commit()
    print("success - insert psm row count: ", len(psmDataSet))
except sqlite3.IntegrityError:
    con.rollback()
    print("ERROR - couldn't insert psm!")

con.isolation_level = None
con.execute('VACUUM')
# <- note that this is the default value of isolation_level
con.isolation_level = ''

con.close()
