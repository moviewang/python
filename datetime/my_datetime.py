import time
import calendar


print(time.time())
print('localtime:', time.localtime(time.time()))
print('localtime:', time.localtime())
print(time.asctime(time.localtime()))

#format data to str
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(type(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))

#str to timestamp
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

print(calendar.month(2017, 9))