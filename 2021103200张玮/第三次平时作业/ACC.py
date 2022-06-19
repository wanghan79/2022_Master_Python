import random
import string
from functools import wraps
from math import sqrt
import torch
from dataFactoryInterface import *

def ACC(decPara):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            num = kwargs.get('num')
            item = {'num': num, 'datarange': (0, 1)}
            interface = dataFactoryInterface()
            ground = interface.create("int")
            ground1 = ground.sampling(**item)
            ground2 = torch.tensor(ground1, dtype=torch.int32)
            predict = interface.create("selfDefinedStruct")
            predict1 = predict.sampling(**kwargs)
            predict_flag = list()
            for item in predict1:
                predict_flag.append(item[3])
            predict2 = torch.tensor(predict_flag, dtype=torch.int32)
            correct = predict2.eq(ground2).sum().item()
            total = num
            print("ACC: {}".format(correct * 100.0 / total))
            return func(**kwargs)
        return wrapper
    return decorator

@ACC("decPara")
def pred1(**struct):
    pass

@ACC("decPara")
def pred2(*args, **struct):
    pass

if __name__ == '__main__':
    paras1 = {'num': 5, 'struct': {
        "int": {'datarange': (0, 100)},
        'float': {"datarange": (0, 100)},
        "str": {'datarange': string.ascii_uppercase, 'strlen': 5},
        "bool": {'datarange': (0, 1)}
    }}
    pred1(**paras1)

    args2 = {'num': 5}
    paras2 = {'num': 5, 'struct': {
        "int": {'datarange': (0, 100)},
        'float': {"datarange": (0, 100)},
        "str": {'datarange': string.ascii_uppercase, 'strlen': 5},
        "bool": {'datarange': (0, 1)}
    }}
    pred2(args2, **paras2)