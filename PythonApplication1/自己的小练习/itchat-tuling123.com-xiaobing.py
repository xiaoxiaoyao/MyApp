import requests,time,random,itchat

#自动把各种聊天内容发给微软小冰isXiaobingChat的小程序（附带图灵机器人和小冰聊天isTuling）
isTuling,isXiaobingChat= True ,True
def get_response(msg):
  Url = 'http://www.tuling123.com/openapi/api'
  data = {
    'key'  :  '75137612d89c42f0b9d7a3f5133ec656', #这个key可以直接拿来用，随便用，无所谓，放心公开
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
  # 如果图灵Key出现问题，那么reply将会是None
  reply = get_response(msg['Text'])
  # a or b的意思是，如果a有内容，那么返回a，否则返回b， 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
  return reply or 'I received: ' + msg.get('Text')

# 微信好友发来的内容isFriendChat=True, 群聊发来的内容isGroupChat=True, 公众号发来的内容isMpChat=False
isFriendChat, isGroupChat , isMpChat=True,True, False
@itchat.msg_register(itchat.content.TEXT, isFriendChat=isFriendChat, isGroupChat=isGroupChat, isMpChat=isMpChat)
def xiaobing(msg):
  # 发送图灵机器人回复内容
  if isTuling:
        time.sleep(random.random()*2)
        itchat.send(tuling_reply(msg),toUserName=itchat.search_mps(name='小冰')[0]['UserName'])
  # 发送之前的内容
  if isXiaobingChat:
        time.sleep(random.random()*3)
        itchat.send(msg['Content'],toUserName=itchat.search_mps(name='小冰')[0]['UserName'])
  del msg # 对象的别名被显式的销毁，引用计数值为0，等待垃圾回收。该释放的变量及时释放，如果不及时释放，长期积累占用内存

if __name__ == '__main__':
  itchat.auto_login()# 命令行则 enableCmdQR=2
  itchat.run()
