class Foo:
    def __init__(self):
        self.__test = 100


foo = Foo()
print(dir(foo))
print(foo._Foo__test)