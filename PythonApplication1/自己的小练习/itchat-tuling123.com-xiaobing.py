import requests,time,random,itchat
def get_response(msg):
  Url = 'http://www.tuling123.com/openapi/api'
  data = {
    'key'  : KEY,
    'info'  : msg,
    'userid' : 'pth-robot',
  }
  try:
    r = requests.post(Url, data=data).json()
    return r.get('text')
  except:
    return

#@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
  # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
  defaultReply = 'I received: ' + msg['Text']
  # 如果图灵Key出现问题，那么reply将会是None
  reply = get_response(msg['Text'])
  # a or b的意思是，如果a有内容，那么返回a，否则返回b
  return reply or defaultReply

# 微信好友发来的内容isFriendChat=True, 群聊发来的内容isGroupChat=True, 公众号发来的内容isMpChat=False
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=True, isMpChat=False)
def xiaobing(msg):
	time.sleep(random.random()*5)
  # 发送图灵机器人回复内容
	itchat.send(tuling_reply(msg),toUserName=itchat.search_mps(name='小冰')[0]['UserName'])
	#time.sleep(random.random()*3)
  # 发送之前的内容
	#itchat.send(msg['Content'],toUserName=itchat.search_mps(name='小冰')[0]['UserName'])
	#time.sleep(random.random()*1)

KEY = '75137612d89c42f0b9d7a3f5133ec656' #这个key可以直接拿来用，随便用，无所谓，放心公开

if __name__ == '__main__':
	itchat.auto_login(enableCmdQR=2)
	itchat.run()
