
#类的方法与函数的区别在与类的方法必须有第一个额外参数self,表示类的实例
class Myclass:
    i = 0
    '''构造方法'''
    def __init__(self, i):
        self.i = i

    def print(self):
        print(self.i)

m = Myclass(10)
print(m.i)
m.print()

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

test = Test()
test.prt()

class people:
    name = ''
    age = 0
    weight = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def say(self):
        print('my name is %s,%s years old, and %s weight' % (self.name, self.age, self.weight))

p = people('jack', 16, 120)
people.say(p)

class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    def say(self):
        print('my name is %s,%s years old, and %s weight,now i am in %s' % (self.name, self.age, self.weight, self.grade))

s = student('jack', 11, 64, 'senior')
s.say()

class speaker:
    topic = ''
    name = ''
    def __init__(self, t, n):
        self.name = n
        self.topic = t
    def say(self):
        print('i am speaker,My name is %s, My topic is %s' % (self.name, self.topic))

s = speaker('hello', 'maria')
s.say()


class sample(speaker, student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, t, n)
sa = sample('Tim', 23, 100, 4, 'python')
sa.say()
