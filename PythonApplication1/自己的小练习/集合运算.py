'''
摘要
1. 总结
1.1 求两个list的交、并、差（补)、对称差集 - 使用set集合运算符
1.2 求两个list的交、并、差（补)、对称差集 - 使用set集合的方法 - 高效率
2.求两list的交集 - 不同实现方式
3.求两个list的并集 - 不同实现方式
4.求两个list的差(补)集 - 不同实现方式
5.求两个list的对称差集 - 不同实现方式

本文主要介绍在Python下求两个list的交集、并集、差（补）集、对称差集的方法。首先，总结了实现上述功能主要的两种方法：1.使用set集合运算符，2.使用set集合的方法（推荐第2种方法）；接着，依次对同一功能的不同种实现方式罗列出具体例子（不限于上述两种方法）。
'''

# 1.1 求两个list的交、并、差（补)、对称差集 - 使用set集合运算符

a = [0,1,2,3,4]
b = [0,2,6]
list(set(a) & set(b))   # 使用  "&"  运算求a与b的交集，输出：[0, 2]
list(set(a) | set(b))   # 使用  "|"  运算求a与b的并集，输出：[0, 1, 2, 3, 4, 6]
list(set(b) - set(a))   # 使用  "-"  运算求a与b的差(补)集： 求b中有而a中没有的元素，输出：[6]
list(set(a) - set(b))   # 使用  "-"  运算求a与b的差(补)集： 求a中有而b中没有的元素，输出：[1, 3, 4]
list(set(a) ^ set(b))   # 使用  "^"  运算求a与b的对称差集，输出：[1, 3, 4, 6]

# 1.2 求两个list的交、并、差（补)、对称差集 - 使用set集合的方法 - 高效率

a = [0,1,2,3,4]
b = [0,2,6]
list(set(a).intersection(set(b)))  # 使用 intersection 求a与b的交集，输出：[0, 2]
list(set(a).union(b))              # 使用 union 求a与b的并集，输出：[0, 1, 2, 3, 4, 6]
list(set(b).difference(set(a)))    # 使用 difference 求a与b的差(补)集：求b中有而a中没有的元素，输出： [6]
list(set(a).difference(set(b)))    # 使用 difference 求a与b的差(补)集：求a中有而b中没有的元素，输出：[1, 3, 4]
list(set(a).symmetric_difference(b))   # 使用 symmetric_difference 求a与b的对称差集，输出：[1, 3, 4, 6]
