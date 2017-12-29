class Student(object):
    """
    # 为了限制score的范围，可以通过一个`set_score()`方法来设置成绩，再通过一个`get_score()`来获取成绩。
    这样，在`set_score()`方法里，就可以检查参数：
    """

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(60)  # ok!
print('s.get_score()', s.get_score())

try:
    s.set_score(9999)  # ValueError: score must between 0 ~ 100!
except ValueError as identifier:
    print(identifier)
finally:
    pass

# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：


class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student2()
s.score = 80  # ok!
print('s.score', s.score)

try:
    s.score = 9999  # ValueError: score must between 0 ~ 100!
except ValueError as identifier:
    print(identifier)
finally:
    pass
