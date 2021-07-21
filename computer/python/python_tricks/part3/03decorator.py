# 一个简单的装饰器
def null_decorator(func):
    return func


def greet():
    return "Hello1!"


greet = null_decorator(greet)
print(greet())


@null_decorator
def greet():
    return "Hello2!"


print(greet())


# 装饰器可以修改行为
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return "Hello!"


print(greet())


# 多个装饰器
def strong(func):
    def wrapper():
        return f"<strong>{func()}</strong>"

    return wrapper


def emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"

    return wrapper


@strong
@emphasis
def greet():
    return "Hello!"


print(greet())


# 装饰器接受参数
def trace(func):
    def wrapper(*args, **kwargs):
        print(f"TRACE: calling {func.__name__}()"
        f"with {args}, {kwargs}")

        original_result = func(*args, **kwargs)

        print(f"TRACE: {func.__name__}()"
        f"returned {original_result!r}")

def  say() 