
from math import sqrt
from selfSamping import *

# 设置用于计算ACC和MCC的对照
target = []
for r in range(100):
    tmp = random.getrandbits(1) # 返回具有指定位数的整数
    target.append(tmp)


# ACC装饰器
def ACC(name):
    def decorator(func):  # 传入修饰的func函数
        def wrapper(*args, **kwargs):
            print("calculate："+name)
            result = func(*args, **kwargs)  # 调用修饰的func函数
            correct = 0
            for i in range(100):
                if len(result[0]) > 1:
                    if result[i][-1] == target[i]: # 如果与对照相等，则预测正确
                        correct += 1
                else:
                    if result[i] == target[i]: # 如果与对照相等，则预测正确
                        correct += 1
            return correct / 100 # 返回acc结果
        return wrapper
    return decorator


# MCC装饰器
def MCC(name):
    def decorator(func):  # 传入修饰的func函数
        def wrapper(*args, **kwargs):
            print("calculate："+name)
            result = func(*args, **kwargs)# 调用修饰的func函数
            tp, fn, fp, tn = 0, 0, 0, 0

            for i in range(100):
                if len(result[0]) > 1:
                    if target[i] == 1:
                        if result[i][-1] == 1:
                            tp += 1
                        else:
                            fn += 1
                    else:
                        if result[i][-1] == 1:
                            fp += 1
                        else:
                            tn += 1
                else:
                    if target[i] == 1:
                        if result[i][-1] == 1:
                            tp += 1
                        else:
                            fn += 1
                    else:
                        if result[i][-1] == 1:
                            fp += 1
                        else:
                            tn += 1
            numerator = (tp * tn) - (fp * fn)  # 计算MCC公式分子
            denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))  # 计算MCC公式分母
            return numerator / denominator # 返回mcc结果
        return wrapper
    return decorator


@ACC("acc")
def resultAcc(struct):
    interface = dataFactoryInterface()
    obj = interface.create("selfDefinedStruct")
    paras = {"num": 100, "struct": {"int": {"dataRange": (0, 10)},
                                    "float": {"dataRange": (0, 20)},
                                    "bool": {}}}
    result = obj.sampling(**paras)
    return result


@MCC("mcc")
def resultMcc(*args, **kwargs):
    interface = dataFactoryInterface()
    result = []
    for i in args:
        if i == "struct":
            obj = interface.create("selfDefinedStruct")
            paras = {"num": 100, "struct": {"int": {"dataRange": (0, 10)},
                                            "float": {"dataRange": (0, 20)},
                                            "bool": {}}}
            result = obj.sampling(**paras)

        else:
            obj = interface.create("bool")
            paras = {"num": 100, "bool": {}}
            result = obj.sampling(**paras)
    return result

"""
测试使用装饰器的函数
"""
if __name__ == '__main__':
    # 计算Acc
    print(resultAcc("struct"))
    # 计算Mcc
    print(resultMcc("struct"))
