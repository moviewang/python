class Parent:
    def my_method(self):
        print('parent method')


class Child(Parent):
    def my_method(self):
        Parent.my_method(self)
        print('child method')


child = Child()
child.my_method()


class JustCounter:
    ___private_count = 0
    public_count = 0

    def count(self):
        # self.___private_counts += 1
        self.public_count += 1
        # print('private_count:', self.___private_count)
        print('public_count:', self.public_count)


j = JustCounter()
print(j.public_count)
j.count()


class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name:', self.name)
        print('url:', self.__url)

    def __foo(self):
        print('name:', self.name)
        print('url:', self.__url)

    def foo(self):
        self.__foo()

s = Site('baidu', '11')
s.who()
s.foo()
# s.__fo/o()

# class Site:
#     def __init__(self, name, url):
#         self.name = name  # public
#         self.__url = url  # private
#
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
#
#     def __foo(self):  # 私有方法
#         print('这是私有方法')
#
#     def foo(self):  # 公共方法
#         print('这是公共方法')
#         self.__foo()
# x = Site('菜鸟教程', 'www.runoob.com')
# x.who()        # 正常输出
# x.foo()        # 正常输出
# x.__foo()      # 报错