import random
import string
from functools import wraps
from math import sqrt
import torch
from dataFactoryInterface import *

def MCC(decPara):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            row = kwargs.get('row')
            col = kwargs.get('col')
            interface = dataFactoryInterface()
            row1 = interface.create("int")
            row2 = row1.sampling(**row)
            col1 = interface.create("int")
            col2 = col1.sampling(**col)
            row3 = torch.tensor(row2, dtype=torch.int32)
            col3 = torch.tensor(col2, dtype=torch.int32)

            TP = row3[row3 == 0].size()[0]
            FP = row3[row3 == 1].size()[0]
            FN = col3[col3 == 1].size()[0]
            TN = col3[col3 == 1].size()[0]

            numerator = (TP * TN) - (FP * FN)
            denominator = sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            result = numerator / denominator
            print("MCC: {}".format(result))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@MCC("decPara")
def pred1(**struct):
    pass

@MCC("decPara")
def pred2(*args, **struct):
    pass

if __name__ == '__main__':
    paras1 = {
        'row': {'num': 5, 'datarange': (0, 1)},
        'col': {'num': 10, 'datarange': (0, 1)}
    }
    pred1(**paras1)

    args2 = {'num': 5}
    paras2 = {
        'row': {'num': 5, 'datarange': (0, 1)},
        'col': {'num': 10, 'datarange': (0, 1)}
    }
    pred2(args2, **paras2)