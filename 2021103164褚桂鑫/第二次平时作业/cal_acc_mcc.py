import random
import string
from functools import wraps
from math import sqrt

import torch

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

            numerator = (TP * TN) - (FP * FN)  # 马修斯相关系数公式分子部分
            denominator = sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))  # 马修斯相关系数公式分母部分
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


if __name__ == '__main__':
    '''
    #验证准确率 acc
    paras1 = {'num': 10, 'struct': {
        "int": {'datarange': (0, 100)},
        'float': {"datarange": (0, 1000)},
        "str": {'datarange': string.ascii_uppercase, 'strlen': 10},
        "bool": {'datarange': (0, 1)}
    }}
    pred1(**paras1)

    args2 = {'num': 30}
    paras2 = {'num': 30, 'struct': {
        "int": {'datarange': (0, 100)},
        'float': {"datarange": (0, 1000)},
        "str": {'datarange': string.ascii_uppercase, 'strlen': 10},
        "bool": {'datarange': (0, 1)}
    }}
    pred2(args2, **paras2)
    '''

    # 验证马修斯相关系数（Matthews correlation coefficient）
    paras1 = {
        'row': {'num': 10, 'datarange': (0, 1)},
        'col': {'num': 8, 'datarange': (0, 1)}
    }
    pred1(**paras1)
    paras2 = {
        'row': {'num': 30, 'datarange': (0, 1)},
        'col': {'num': 50, 'datarange': (0, 1)}
    }
    args2 = {'num': 30}
    pred2(args2, **paras2)
