import math
import random


class dataFactory(object):

    def __init__(self):
        self.__name = 'dataFactory'

    def sampling(self, **kwargs):
        raise Exception("This is a base factory")


class dataFactoryInterface(object):

    def __init__(self):
        self.__name = 'dataFactoryInterface'

    def create(self, target):
        classname = target + 'Sampling'
        return eval(classname)()


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


class selfDefinedClassSampling(dataFactory):

    def __init__(self):
        self.__name = 'selfDefinedClassSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result


# Matrix
class GetMatrix():
    def __init__(self):
        self.__name = 'GetMatrix'

    def get_all(self, *args):
        int_list = args[0].get('int')
        float_list = args[0].get('float')
        bool_list = args[0].get('bool')
        num = args[0].get('num')
        tp, fp, tn, fn = 0, 0, 0, 0
        for i in range(0, num):
            if bool_list[i] == 1:
                if int_list[i] <= float_list[i]:
                    tp += 1
                else:
                    fp += 1
            else:
                if int_list[i] <= float_list[i]:
                    tn += 1
                else:
                    fn += 1
        return tp, fp, tn, fn


class Decorator():
    def __init__(self, func):
        self._func = func
        self.matrix = GetMatrix()

    def __call__(self, *args, **kwargs):
        tp, fp, tn, fn = self.matrix.get_all(*args)
        mcc = float(tp * tn - fp * fn) / (
            math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))) + float(0.000001)
        acc = float((tp + tn) / (tp + tn + fp + fn))
        self._func(*args, **kwargs)
        # print('mcc:'+str(mcc)+' acc:'+str(acc))
        return str(mcc), str(acc)


@Decorator
def pred1(dic):
    print(dic)


@Decorator
def pred2(*args, **kwargs):
    print(args, **kwargs)


if __name__ == '__main__':
    name_list = ['int', 'float', 'bool']
    value_dic = {}
    interface = dataFactoryInterface()
    paras = {'datarange': (0, 10), 'num': 5}
    value_dic['num'] = paras.get('num')

    for name in name_list:
        obj = interface.create(name)
        result = obj.sampling(**paras)
        value_dic[name] = result
    mcc, acc = pred1(value_dic)
    print('pred1:\nacc:' + acc, '\nmcc:' + mcc)

    name_list = ['int', 'float', 'bool']
    value_dic = {}
    interface = dataFactoryInterface()
    paras = {'datarange': (0, 10), 'num': 5}
    value_dic['num'] = paras.get('num')

    for name in name_list:
        obj = interface.create(name)
        result = obj.sampling(**paras)
        value_dic[name] = result
    mcc, acc = pred2(value_dic)
    print('pred2:\nacc:' + acc, '\nmcc:' + mcc)
