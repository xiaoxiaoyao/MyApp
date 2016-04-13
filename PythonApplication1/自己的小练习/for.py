# -*- coding: utf-8 -*-

counter=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

print('''
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

if you use for
it will be:''')
for item in counter:
    print(item)
    if item==5:
        item=counter[8]
    print(item)

#修改循环对象的值是C的思维方式，最好不要用在写python代码上。
#应当使用while

print('''
you should use while
it will be:''')
i = 0
length = len(counter)
while i < length:
    #just do it
    print(counter[i])
    if i==5:
        i=counter[8]
    print(counter[i])
    i += 1