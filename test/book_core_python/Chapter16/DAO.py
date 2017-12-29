# -*- coding:utf-8 -*-
# file: DAO.py
#
import win32com.client								# 导入win32com.client
dbEngine = win32com.client.Dispatch('DAO.DBEngine.35')				# 连接COM对象
daoDB = dbEngine.OpenDatabase('python.mdb')					# 打开数据库
daoRS = daoDB.OpenRecordset('people')						# 打开表
daoRS.MoveLast()     								# 移动到最后一条记录
print daoRS.RecordCount								# 输出记录总数
print daoRS.Fields('name').Value						# 输出最后一条记录的name
print daoRS.Fields('age').Value							# 输出最后一条记录的age
print daoRS.Fields('sex').Value							# 输出最后一条记录的sex
daoRS.AddNew()									# 添加新记录
daoRS.Fields('name').Value = 'Kate'						# 新记录的name
daoRS.Fields('age').Value = 22							# 新记录的age
daoRS.Fields('sex').Value = 'Female'						# 新记录的sex
daoRS.Update()									# 更新记录
daoRS.Close()									# 关闭表
daoDB.Close()									# 关闭数据库连接
