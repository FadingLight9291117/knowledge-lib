"""
1. 函数是对象
2. 函数可以存储在数据结构中
3. 函数可传递给其他函数
4. 函数可以嵌套
5. 函数可捕获局部状态(闭包)
6. 对象可作为函数使用
"""


def yell(text):
    return text.upper() + '!'


print(yell("hello"))

bark = yell

print(bark("hello"))

del yell


# 函数可以存入列表
funcs = [bark, str.lower, str.capitalize]

for f in funcs:
    print(f, f("hey there"))


# 对象可以作为函数调用
class Foo:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(self.name)


foo = Foo("clz")

foo()
