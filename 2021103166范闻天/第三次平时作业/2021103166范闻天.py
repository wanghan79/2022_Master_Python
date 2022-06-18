import random
import numpy as np
import math
from functools import wraps

def creatData(struct):
    result = []
    for x in range(0, 200):
        data = []
        if struct[0] is int:
            data.append(random.randint(0, 10))
        else:
            data.append(None)
        if struct[1] is float:
            data.append(random.uniform(0, 20))
        else:
            data.append(None)
        if struct[2] is bool:
            data.append(random.randint(0, 1))
        else:
            data.append(None)
        result.append(tuple(data))
    return result
def confusion_matrix(data,label):
    lengh=len(data)
    tp = 0
    tn = 0
    fn = 0
    fp = 0
    for x in range(0, lengh):
        if label[x] == 1:
            if data[x][2] == label[x]:
                tp = tp + 1
            else:
                fn = fn + 1
        else:
            if data[x][2] == label[x]:
                tn = tn + 1
            else:
                fp = fp + 1
    return tp,tn,fn,fp
#Acc = (TP+TN)/(TP+FN+TN+FP)
def ACC(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data,label=func(*args, **kwargs)
        tp,tn,fn,fp=confusion_matrix(data,label)
        Acc = (tp + tn) / (tp + fn + tn + fp)
        print('ACC:%.3f'%Acc)
    return wrapper
#MCC=(TP*TN-FP*FN)/sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
def MCC(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data,label=func(*args, **kwargs)
        TP,TN,FN,FP=confusion_matrix(data,label)
        MCC=(TP*TN-FP*FN)/math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
        print('MCC:%.3f'%MCC)
        return data,label
    return wrapper
#调用两个装饰器，先调用后执行完，后调用先执行完。
@ACC
@MCC
def pred1(struct):
    data=creatData(struct)
    label = np.random.randint(0, 2, size=len(data))
    return data,label
def pred2(*args, **kwargs):
    data=creatData(args)
    label = np.random.randint(0, 2, size=len(data))
    return data,label
print("========执行pred1========")
pred1([int,float,bool])
print("========执行pred2========")
pred1([int,float,bool])

