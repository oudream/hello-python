# -*- coding:utf-8 -*-
# file: gtalk.py
#
import xmpp									# 导入模块
def GetMessage(client, message):						# 消息处理函数
	text = message.getBody()						# 获得消息内容
	people = message.getFrom()						# 获得发信者
	print 'GET: %s FROM: %s' % (text, people)				# 打印消息
	client.send(xmpp.protocol.Message(people,				# 发送消息
		'GET: ' + text,typ="chat"))
user = raw_input('User:')							# 获取用户名
password = raw_input('Password:')						# 获取密码
jid = xmpp.protocol.JID(user + '@gmail.com')					# 创建JID
client = xmpp.Client(jid.getDomain(),debug=[])					# 创建客户端
client.connect(('talk.google.com',5222))					# 连接服务器
client.auth(user, password)							# 用户认证
Roster = client.getRoster()							# 获取用户列表
names = Roster.getItems()							# 获取用户名
for name in names:								# 循环输出用户
    status = Roster.getStatus(name)
    print name,
    print status
client.RegisterHandler('message',GetMessage)					# 注册消息回调函数
client.sendInitPresence()							# 设置在线
while 1:									# 进入循环
	try:
		client.Process(1)
	except KeyboardInterrupt:						# 处理Ctrl+c
		break
