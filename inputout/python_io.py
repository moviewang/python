import math

f = open('tmp.txt', 'r+')
num = f.write('ss')
print(num)
str = f.read()
print('tmp:', type(str), str)
f.close()
print(math.sin(1))