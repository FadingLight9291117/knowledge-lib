
errno = 50159747054
name = "Bob"

# 旧式
str1_1 = "Hello %s, there is a 0x%x error!" % (name, errno)
str1_2 = "Hello %(name)s, there is a 0x%(errno)x error!" % {"name": name, "errno": errno}   # 别名传递

# 新式
str2_1 = "Hello， {}, there is a 0x{:x} error!".format(name, errno)
str2_2 = "Hello, {name}, there is a 0x{errno:x} error!".format(name=name, errno=errno)

# 格式化字符串字面值 python 3.6+
str3_1 = f"Hello, {name}, there is a {errno:#x} errors!"
a = 5
b = 10
str3_2 = f"Five plus ten is {a + b} and not {2 * (a + b)}"  # 可以嵌入表达式


# 模板字符串，更安全
from string import Template
t = Template("Hello, $name!")
t.substitute(name=name)


# 下面演示不安全
class Foo:
    def __init__(self):
        self.name = "clz"
foo = Foo()
strst = "{foo.name}".format(foo=foo)
print(strst)