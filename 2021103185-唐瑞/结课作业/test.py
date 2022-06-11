def dec1(func):
    print("dec1装饰函数")
    def one():
        print("2222")
        func()
        print("3333")
    return one


def dec2(func):
    print("dec2装饰函数")
    def two():
        print("bbbb")
        func()
        print("cccc")

    return two

@dec1
@dec2
def test():
    print("test test")

test()
