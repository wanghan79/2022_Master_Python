import math
import random
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        sum = 0
        for item in result:
            if item[1]:
                sum = sum + 1
        print("准确率：{}".format(sum / len(result)))
        return result
    return wrapper
def decorator1(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        for item in result:
            if item[2] == item[1] == 1:
                TP =TP+1
            if item[2] == 1 and item[1] == 0:
                FP = FP + 1
            if item[2] == 0 and item[1] == 1:
                FN = FN + 1
            if item[2] == item[1] == 0:
                TN = TN + 1
        mcc=(TP*TN-FP*FN)/(math.pow((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN), 0.5))
        print("马修斯相关系数{}".format(mcc))
        return result
    return wrapper
def sampling(**kwargs):
    result = list()
    for index in range(0, 100):
        element = list()
        for key, value in kwargs.get("struct").items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "trueLable":
                tmp = random.randint(0, 1)
            elif key == "preLable":
                tmp = random.randint(0, 1)
            else:
                break
            element.append(tmp)
        result.append(element)
    return result
def samplings(struct):
    result = list()
    for index in range(0, 100):
        element = list()
        for key, value in struct.items():
            if key == "int":
                it=iter(value['datarange'])
                tmp=random.randint(next(it),next(it))
            elif key == "preLable":
                tmp = random.randint(0, 1)
            elif key == "trueLable":
                tmp = random.randint(0, 1)
            else:
                    break
            element.append(tmp)
        result.append(element)
    return result
if __name__ == "__main__":
    paras = {"struct": {"int": {"datarange": (0, 100)}, "preLable": {}, "trueLable": {}}}
    print("acc准确率###############################################")
    dec = decorator(sampling)
    result = dec(**paras)

    print("mcc相关系数##############################################")
    dec1 = decorator1(sampling)
    result = dec1(**paras)

    print("acc准确率################################################")
    dec = decorator(samplings)
    result = dec(**paras)

    print("mcc相关系数###############################################")
    dec1 = decorator1(samplings)
    result = dec1(**paras)

