#把数据都存云上，你们说吼不吼啊
import leancloud
appid=input("https://console.qcloud.com/tab#{{appid}}")
appkey=input("{{appkey}}")
leancloud.init(appid,appkey)

from leancloud import Object,LeanCloudError
class douban(Object):
    """description of class"""
    def is_cheated(self):
        # 可以像正常 Python 类一样定义方法
        return self.get('cheatMode')

    @property
    def pid(self):
        # 可以使用property装饰器，方便获取属性
        return self.get('score')

    @score.setter
    def pid(self, value):
        # 同样的，可以给对象的score增加setter
        return self.set('score', value)


