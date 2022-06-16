import string
from dataFactoryInterface import dataFactoryInterface
from ACC_Calculating import *
from MCC_Calculating import *
from functools import wraps
@ACC
def predACC(*args, **kwargs):
    pass


@MCC
def predMCC(*args, **kwargs):
    pass


if __name__ == "__main__":
    interface = dataFactoryInterface()
    class_list = ['int', 'float','bool']
    dicts = {}
    interface = dataFactoryInterface()
    paras = {'datarange': (0, 10), 'num': 100}
    dicts['num'] = paras.get('num')
    for name in class_list:
        obj = interface.create(name)
        result = obj.sampling(**paras)
        dicts[name] = result
    acc = predACC(dicts)
    mcc = predMCC(dicts)
    print('ACC:%.6f'%acc)
    print('MCC:%.6f'%mcc)