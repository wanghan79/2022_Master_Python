

# Calling other function as a parameter
import logging


def foo():
    print("This is foo")


def bar(func):
    func()


bar(foo)


# An expended logging method using function calling
def addLogging(func):
    logging.warning("%s is running" % func.__name__)
    func()


addLogging(foo)


# Wrap the function calling in a function
def addLogging(func):
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()
    return wrapper


foo = addLogging(foo)
foo()


# The first decorator in Python
@addLogging
def foo():
    print("This is a decorated foo")


foo()


# The decorator with parameters
def addLogging(decPara):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@addLogging("A level")
def foo(name="mike"):
    print("The name in foo is %s" % name)


@addLogging("A level")
def doo(paraA, paraB, *args):
    print(paraA, paraB, *args)


foo("aaa")
doo("paraA", "paraB", ("argsA", "argsB"))


# Using Python decorator @wraps
from functools import  wraps


def addLogging(decPara):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@addLogging("decPara")
def foo(*args):
    print(foo.__name__)
    print(args)


foo(1, 2, 3)


# Class decorator
class DecoratorClass():
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        self._func(*args, **kwargs)


@DecoratorClass
def foo(*args):
    print(args)


foo(1, 2, 3)

