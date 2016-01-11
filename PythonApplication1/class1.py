class my_class(object):

    def __init__(self, name, score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))



