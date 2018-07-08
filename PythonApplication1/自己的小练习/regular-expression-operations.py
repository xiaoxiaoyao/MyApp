# -*- coding: utf-8 -*-  
#一个简单的re(Regular expression operations正则表达式)实例，匹配字符串中的hello字符串  
  
#导入re(Regular expression operations)模块  
import re
   
# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”  
pattern = re.compile(r'hello')  
   
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None  
match1 = pattern.match('hello world!')  
match2 = pattern.match('helloo world!')  
match3 = pattern.match('helllo world!')  
  
#如果match1匹配成功  
if match1:  
    # 使用Match获得分组信息  
    print(match1.group())
else:  
    print('match1匹配失败！')
  
  
#如果match2匹配成功  
if match2:  
    # 使用Match获得分组信息  
    print(match2.group())
else:  
    print('match2匹配失败！')
  
  
#如果match3匹配成功  
if match3:  
    # 使用Match获得分组信息  
    print(match3.group())
else:  
    print('match3匹配失败！')

# 附上几个网上搜到的验证Url地址的正则表达式
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

# 关于python使用re模块的第三个参数简单了解

# re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法）
#        re.M(re.MULTILINE): 多行模式，改变'^'和'$'的行为
#        re.S(re.DOTALL): 点任意匹配模式，改变'.'的行为
