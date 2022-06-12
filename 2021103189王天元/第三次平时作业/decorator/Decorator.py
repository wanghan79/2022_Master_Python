
import math
import random
"""
create by wty
2022/6/2
"""

class dataFactoryInterface(object):

    def __init__(self):
        self.__name = 'dataFactoryInterface'

    def create(self, target):
        classname = target + 'Sampling'
        return eval(classname)()


class dataFactory(object):

    def __init__(self):
        self.__name = 'dataFactory'

    def sampling(self, **kwargs):
        raise Exception("This is a base factory")


class intSampling(dataFactory):

    def __init__(self):
        self.__name = 'iniSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        return result


class floatSampling(dataFactory):

    def __init__(self):
        self.__name = 'floatSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.uniform(next(it), next(it))
            result.append(tmp)
        return result


class boolSampling(dataFactory):

    def __init__(self):
        self.__name = 'boolSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.getrandbits(1)
            result.append(tmp)
        return result


class matrix_value():
    def get_value(self, *args):
        int_value = args[0]['int']
        float_value = args[0]['float']
        bool_value = args[0]['bool']
        num = args[0]['num']
        tp, fp, tn, fn = 0, 0, 0, 0
        for i in range(0, num):
            if bool_value[i] == 1:
                if int_value[i] <= float_value[i]:
                    tp = tp + 1
                else:
                    fp = fp + 1
            else:
                if int_value[i] <= float_value[i]:
                    tn = tn + 1
                else:
                    fn = fn + 1
        return tp, fp, tn, fn


class MCC():
    def __init__(self, func):
        self.funcs = func
        self.matrix = matrix_value()

    def __call__(self, *args, **kwargs):
        tp, fp, tn, fn = self.matrix.get_value(*args)
        mcc = float(tp * tn - fp * fn) / (math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))) + float(0.000001)
        self.funcs(*args, **kwargs)
        return mcc


class ACC():
    def __init__(self, func):
        self.funcs = func
        self.matrix = matrix_value()

    def __call__(self, *args, **kwargs):
        tp, fp, tn, fn = self.matrix.get_value(*args)
        acc = float((tp + tn) / (tp + tn + fp + fn))
        self.funcs(*args, **kwargs)
        return acc


@ACC
def pred1(*args, **kwargs):
    print(args, **kwargs)


@MCC
def pred2(*args, **kwargs):
    print(args, **kwargs)


if __name__ == '__main__':
    class_list = ['int', 'float', 'bool']
    dicts = {}
    interface = dataFactoryInterface()
    paras = {'datarange': (0, 10), 'num': 10}
    dicts['num'] = paras.get('num')
    for name in class_list:
        obj = interface.create(name)
        result = obj.sampling(**paras)
        dicts[name] = result
    acc = pred1(dicts)
    mcc = pred2(dicts)
    print(f'acc:{acc}')
    print(f'mcc:{mcc}')
