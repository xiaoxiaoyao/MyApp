import itchat, time, random
# 群发内容（随机选一条）
SINCERE_WISH = [u'祝中秋快乐',u'中秋快乐呀',u'中秋快乐哟',u'中秋节快乐呀~',u'中秋节快乐!',u'中秋国庆快乐!']
itchat.auto_login(True)
i=1
friendList = itchat.get_friends(update=True)[i:]


for friend in friendList:
	try:
		# 祝福语中随机选一条
		n=random.randint(0,len(SINCERE_WISH)-1)
		# 如果是演示目的，把下面的 itchat.send 方法改为 print 即可
		itchat.send(SINCERE_WISH[n], friend['UserName'])
		print(SINCERE_WISH[n], friend['UserName'])
		# print(friend['DisplayName'] or friend['NickName'])
		#为了防止封号
		time.sleep(1+random.random()*124)
	except Exception:# 用于解决异常情况
		print(Exception,":")
		print('ERROR!')
		friend
	finally:
		# 计数
		i=i+1
