import random
from math import sqrt
from selfSamping import *

label = []
for r in range(100):
    tmp = random.getrandbits(1)
    label.append(tmp)


def ACC(name):  # 修饰器的参数
    def decorator(func):  # func为要修饰的函数对象
        def wrapper(*args, **kwargs):
            print(name)
            pred = func(*args, **kwargs)  # 执行函数
            correct = 0
            acc = 0
            for i in range(100):
                if len(pred[0]) > 1:
                    if pred[i][-1] == label[i]:
                        correct += 1
                else:
                    if pred[i] == label[i]:
                        correct += 1
                acc = correct / 100
            return acc

        return wrapper

    return decorator



@ACC("acc")
def pred1(struct):
    interface = dataFactoryInterface()
    obj = interface.create("selfDefinedStruct")
    paras = {"num": 100, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 100)},
                                    "bool": {}}}
    result = obj.sampling(**paras)
    return result



@ACC("acc")
def pred2(*args, **kwargs):
    interface = dataFactoryInterface()
    result = []
    for i in args:
        if i == "struct":
            obj = interface.create("selfDefinedStruct")
            paras = {"num": 100, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 100)},
                                            "bool": {}}}
            result = obj.sampling(**paras)

        else:
            obj = interface.create("bool")
            paras = {"num": 100, "bool": {}}
            result = obj.sampling(**paras)

    return result


print(pred1("struct"))
print(pred2("struct"))
