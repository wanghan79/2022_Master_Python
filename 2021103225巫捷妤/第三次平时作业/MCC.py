import random
from math import sqrt
from selfSamping import *

label = []
for r in range(100):
    tmp = random.getrandbits(1)
    label.append(tmp)


def MCC(name):  # 修饰器的参数
    def decorator(func):  # func为要修饰的函数对象
        def wrapper(*args, **kwargs):
            print(name)
            pred = func(*args, **kwargs)
            tp, fn, fp, tn = 0, 0, 0, 0
            correct = 0
            for i in range(100):
                if len(pred[0]) > 1:
                    if label[i] == 1:
                        if pred[i][-1] == 1:
                            tp += 1
                        else:
                            fn += 1
                    else:
                        if pred[i][-1] == 1:
                            fp += 1
                        else:
                            tn += 1
                else:
                    if label[i] == 1:
                        if pred[i][-1] == 1:
                            tp += 1
                        else:
                            fn += 1
                    else:
                        if pred[i][-1] == 1:
                            fp += 1
                        else:
                            tn += 1
            numerator = (tp * tn) - (fp * fn)  # 马修斯相关系数公式分子部分
            denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))  # 马修斯相关系数公式分母部分
            result = numerator / denominator
            return result

        return wrapper

    return decorator


@MCC("mcc")
def pred1(struct):
    interface = dataFactoryInterface()
    obj = interface.create("selfDefinedStruct")
    paras = {"num": 100, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 100)},
                                    "bool": {}}}
    result = obj.sampling(**paras)
    return result

@MCC("mcc")
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
