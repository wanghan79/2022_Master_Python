def decorator(func):
    def inner(*args, **kwargs):
        print('I am doing some boring work before executing a_func()')
        res = func(*args, **kwargs)
        print('I am doing some boring work after executing a_func()')
        return res
    return inner

class test(object):
    def __init__(self):
        self.__name = "test"
    def run(self):
        print('runing')
        return 0
if __name__ == "__main__":
    t = test()
    t.run()
    run = decorator(t.run)
    run()

