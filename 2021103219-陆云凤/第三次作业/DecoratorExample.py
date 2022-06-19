import math
import random
import string
import logging

class dataFactory1(object):

    def __init__(self):
        self.__name = 'dataFactory1'

    def create(self, target):
        classname = target + 'Sampling'
        return eval(classname)()


class dataFactory(object):

    def __init__(self):
        self.__name = 'dataFactory'

    def sampling(self, **kwargs):
        raise Exception("This is a base factory")


class Sampling1(dataFactory):

    def __init__(self):
        self.__name = 'Sampling1'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        return result


class Sampling2(dataFactory):

    def __init__(self):
        self.__name = 'Sampling2'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.uniform(next(it), next(it))
            result.append(tmp)
        return result



class selfDefinedClassSampling(dataFactory):

    def __init__(self):
        self.__name = 'selfDefinedClassSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result



class Decorator():
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        tp, fp, tn, fn = self.matrix.get_all(*args)
        mcc = float(tp * tn - fp * fn) / (
            math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))) + float(0.000001)
        acc = float((tp + tn) / (tp + tn + fp + fn))
        self._func(*args, **kwargs)
        # print('mcc:'+str(mcc)+' acc:'+str(acc))
        return str(mcc), str(acc)




if __name__ == '__main__':
    name_list = ['int', 'float', 'bool']
    value_dic = {}
    interface = dataFactory1()
    paras = {'datarange': (0, 10), 'num': 10}
    value_dic['num'] = paras.get('num')

    for name in name_list:
        obj = interface.create(name)
        result = obj.sampling(**paras)
        value_dic[name] = result
    mcc, acc = pred(value_dic)
    print('pred:acc:' + acc, 'mcc:' + mcc)