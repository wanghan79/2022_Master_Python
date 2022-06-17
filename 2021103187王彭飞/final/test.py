def dec1(func):
    print("dec1装饰函数")
    def one():
        print("运行之前")
        func()
        print("运行之后")
    return one
def dec2(func):
    print("dec2装饰函数")
    def two():
        print("运行之前")
        func()
        print("运行之后")
    return two
@dec1
@dec2
def test():
    print("test")
test()

