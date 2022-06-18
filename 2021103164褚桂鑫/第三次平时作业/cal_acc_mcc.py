import torch
import random
from functools import wraps
from math import sqrt
from 第二次平时作业.dataFactoryInterface import dataFactoryInterface

def ACC(decPara):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("%s is running" % func.__name__)
            print("参数值 args:{},kwargs:{}".format(args, kwargs))
            random.seed(123)
            total = 0
            correct = 0
            # 获取真实值
            num = kwargs.get('num')
            item = {'num': num, 'datarange': (0, 1)}
            interface = dataFactoryInterface()
            ground_create = interface.create("int")
            ground_truth = ground_create.sampling(**item)
            ground_tensor = torch.tensor(ground_truth, dtype=torch.int32)

            predict_create = interface.create("selfDefinedStruct")
            predict = predict_create.sampling(**kwargs)
            predict_flag = list()
            for item in predict:
                predict_flag.append(item[3])
            predict_tensor = torch.tensor(predict_flag, dtype=torch.int32)
            correct = predict_tensor.eq(ground_tensor).sum().item()
            total = num
            print("acc: {}".format(correct * 100.0 / total))
            return func(**kwargs)

        return wrapper

    return decorator


def MCC(decPara):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global result
            print("%s is running" % func.__name__)
            print("参数值 args:{},kwargs:{}".format(args, kwargs))
            random.seed(123)
            row = kwargs.get('row')
            col = kwargs.get('col')
            interface = dataFactoryInterface()
            row_create = interface.create("int")
            row_ = row_create.sampling(**row)

            col_create = interface.create("int")
            col_ = col_create.sampling(**col)

            row_ = torch.tensor(row_, dtype=torch.int32)
            col_ = torch.tensor(col_, dtype=torch.int32)

            TP = row_[row_ == 0].size()[0]
            FP = row_[row_ == 1].size()[0]
            FN = col_[col_ == 1].size()[0]
            TN = col_[col_ == 1].size()[0]

            # 马修斯相关系数公式分子部分
            numerator = (TP * TN) - (FP * FN)
            # 马修斯相关系数公式分母部分
            denominator = sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            result = numerator / denominator
            print("mcc: {}".format(result))
            return func(*args, **kwargs)

        return wrapper

    return decorator


# @ACC("decPara")
@MCC("decPara")
def pred1(**struct):
    print("first over")


# @ACC("decPara")
@MCC("decPara")
def pred2(*args, **struct):
    print("second over")


