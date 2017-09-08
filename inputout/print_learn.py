import math


#str()返回用户易读的表达形式，repr()返回解释器易读的表达形式,可以python中的任何对象
print(str('hello world'))
print(repr('hello world'))
print(str(1/7))
print(repr(1 / 7))

hellos = 'hello\n'
print(str(hellos))
print(repr(hellos))

print('{0:.3f}'.format(math.pi))

str = input('please input')
print('yours input str is {}'.format(str))

f = open('tmp.txt', 'w')
f.writelines('python is best programing language!')
f.close()