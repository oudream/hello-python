# -*- coding:utf-8 -*-
# file: ADO.py
#
import win32com.client								# 导入win32com.client
adoCon = win32com.client.Dispatch('ADODB.Connection')				# 创建连接对象
adoCon.Open('podbc')  								# 连接到数据源
adoRS = win32com.client.Dispatch('ADODB.Recordset')				# 创建Recordset对象
adoRS.Open('[' + 'people' + ']', adoCon, 1, 3)					# 打开数据源中的people表
adoRS.MoveFirst()								# 移动到第一条记录
for i in range(adoRS.RecordCount):
	print adoRS.Fields('name').Value					# 输出记录的name
	print adoRS.Fields('age').Value						# 输出记录的age
	print adoRS.Fields('sex').Value						# 输出记录的sex
	adoRS.MoveNext()
adoRS.AddNew()									# 添加新记录
adoRS.Fields('name').Value = 'Kate'						# 新记录的name
adoRS.Fields('age').Value = 22							# 新记录的age
adoRS.Fields('sex').Value = 'Female'						# 新记录的sex
adoRS.Update()									# 更新记录
adoRS.Close()									# 关闭表
adoCon.Close()									# 关闭数据库连接
