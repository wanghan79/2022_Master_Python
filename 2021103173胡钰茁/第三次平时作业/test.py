
def decorator(func):
    def inner(*args, **kwargs):
        print('before...........')
        res = func(*args, **kwargs)
        print('after............')
        return res
    return inner

class test(object):
    def __init__(self):
        self.__name = "test"

    def run(self):
        print('run...............')
        return 0

if __name__ == "__main__":
    t = test()
    t.run()
    run = decorator(t.run)
    run ()
    # run.__name__
    # 此时decorator叫做装饰器
