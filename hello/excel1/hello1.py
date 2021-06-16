# pip install pandas xlrd

import pandas as pd
import sqlite3

xls = pd.ExcelFile(r"C:\tmp\u1\limi1.xls")  # use r before absolute file path

sheetX = xls.parse("Sheet1")  # 2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis

print("输出列标题", sheetX.columns.values)

# 	*设备名称	*电压等级	设备类型名称	运行编号	*变电站名称	间隔单元	备注	*设备增加方式	资产编号	资产移交清册ID
var1 = sheetX['间隔单元']

print(var1)  # 1 is the row number..
print("Row Count: ", len(var1.index))  # 1 is the row number..

# print(var1[1]) #1 is the row number..

con = sqlite3.connect('limi.db')

cur = con.cursor()

try:
    cur.execute("insert into lang values (NULL, ?, ?)", ("C", 1972))
    # The qmark style used with executemany():
    lang_list = [
        ("Fortran", 1957),
        ("Python", 1991),
        ("Go", 2009),
    ]
    cur.executemany("insert into lang values (NULL, ?, ?)", lang_list)
    # commit
    con.commit()
    print("insert data success")
except sqlite3.IntegrityError:
    con.rollback()
    print("couldn't add Python twice")

# And this is the named style:
cur.execute("select * from lang where f2=:year", {"year": 1972})
print(cur.fetchall())

con.close()
