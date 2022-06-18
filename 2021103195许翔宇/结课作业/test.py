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

# 两个装饰器就是把函数多次装饰，从下向上装饰，dec2->dec1。然后dec1中func就是被装饰后的函数相当于two()。
# 所以执行结果是
# 2222
# bbbb
# test test
# cccc
# 3333
# 但是因为dec2先装饰，然后dec1再装饰所以先执行
# print("dec2装饰函数")
# 然后再执行
# print("dec1装饰函数")

test()

# 1111
# aaaa
# bbbb
# 2222
# test test
# 3333
# cccc
