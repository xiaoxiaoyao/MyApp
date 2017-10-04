import itchat, time, random
# 群发内容（随机选一条）
SINCERE_WISH = [u'祝中秋快乐',u'中秋快乐呀',u'中秋快乐哟',u'中秋节快乐呀~',u'中秋节快乐!',u'中秋国庆快乐!']
itchat.auto_login(True)
i=1
friendList = itchat.get_friends(update=True)[i:]

print('即将给',len(friendList),'个好友发送中秋祝福，祝福内容为以下随机挑一个：\n',SINCERE_WISH)

for friend in friendList:
	# 祝福语中随机选一条
	SEND_WISH=random.choice(SINCERE_WISH)
	try:
		# 如果是演示目的，把下面的 itchat.send 方法改为 print 即可
		itchat.send(SEND_WISH, friend['UserName'])
		print(friend['UserName'],'\n第',i,'个好友已经成功发送，发送内容为',SEND_WISH)
		# print(friend['DisplayName'] or friend['NickName'])
		# 为了防止封号，自动延时发送
		time.sleep(1+random.random()*124)
	except Exception:# 用于解决异常情况
		print(Exception,":")
		print('ERROR!\n第',i,'个好友发送失败，以下是详细信息')
		friend
	finally:
		# 计数
		i=i+1
