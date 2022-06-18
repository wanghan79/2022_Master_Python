

# Calling other function as a parameter
import string
import logging
import math
import random


def decorator(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        sum = 0
        for item in result:
            if item[3]:
                sum = sum + 1
        print("准确率为{}".format(sum / len(result)))
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
            if item[3] ==1 and item[2]==1:
                TP=TP+1
            if item[3] == 1 and item[2] == 0:
                FP = FP + 1
            if item[3] == 0 and item[2] == 1:
                FN = FN + 1
            if item[3] == 0 and item[2] == 0:
                TN = TN + 1
        mcc=(TP*TN-FP*FN)/(math.pow((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN),0.5))
        print("马修斯相关系数为{}".format(mcc))
        return result
    return wrapper



def sampling(*args,**kwargs):
    result = list()


    for index in range(0,100):
        element = list()
        for key,value in kwargs.get("struct").items():
            if key == "int":
                if not isinstance(value['datarange'][0], int):  # 判断是否为整型数字
                    raise Exception("随机数范围必须为整型数字")
                if not isinstance(value['datarange'][1], int):  # 判断是否为整型数字
                    raise Exception("随机数范围必须为整型数字")

                it=iter(value['datarange'])
                tmp=random.randint(next(it),next(it))
            elif key == "float":
                if not isinstance(value['datarange'][0], int):  # 判断是否为整型数字
                    raise Exception("随机数范围必须为整型数字")
                if not isinstance(value['datarange'][1], int):  # 判断是否为整型数字
                    raise Exception("随机数范围必须为整型数字")
                it=iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key=="str":
                 if not isinstance(value['datarange'], str):
                      raise Exception("随机数范围必须为字符串")
                 if not isinstance(value['strlen'], int):  # 判断是否为整型数字
                    raise Exception("长度必须为整型数字")
                 tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen']))
            elif key == "bool":
                tmp = random.randint(0,1)
            elif key == "lable":
                tmp = random.randint(0,1)
            else:
                    break
            element.append(tmp)
        result.append(element)
    return result

def sampling1(struct):
    result = list()

    for index in range(0,100):
        element = list()
        for key,value in struct.items():
            if key == "int":
                if not isinstance(value['datarange'][0], int):  # 判断是否为整型数字
                    raise Exception("随机数范围必须为整型数字")
                if not isinstance(value['datarange'][1], int):  # 判断是否为整型数字
                    raise Exception("随机数范围必须为整型数字")

                it=iter(value['datarange'])
                tmp=random.randint(next(it),next(it))
            elif key == "float":
                if not isinstance(value['datarange'][0], int):  # 判断是否为整型数字
                    raise Exception("随机数范围必须为整型数字")
                if not isinstance(value['datarange'][1], int):  # 判断是否为整型数字
                    raise Exception("随机数范围必须为整型数字")
                it=iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key=="str":
                 if not isinstance(value['datarange'], str):
                      raise Exception("随机数范围必须为字符串")
                 if not isinstance(value['strlen'], int):  # 判断是否为整型数字
                    raise Exception("长度必须为整型数字")
                 tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen']))
            elif key == "bool":
                tmp = random.randint(0,1)
            elif key == "lable":
                tmp = random.randint(0,1)
            else:
                    break
            element.append(tmp)
        result.append(element)
    return result


if __name__ == "__main__":
    paras = { "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 10000)},
                                "lable":{} ,"bool":{}}}
    # result =sampling(**paras)
    # print(result)
    print("#######################")
    dec=decorator(sampling)
    result = dec(**paras)
    print(result)
    print("#####################")
    dec1=decorator1(sampling)
    result = dec1(**paras)
    print(result)
    print("#####################")
    dec=decorator(sampling1)
    result = dec(**paras)
    print(result)
    print("#####################")
    dec1=decorator1(sampling1)
    result = dec1(**paras)
    print(result)
    print("#####################")