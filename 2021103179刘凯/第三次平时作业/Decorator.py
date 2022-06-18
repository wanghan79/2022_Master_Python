import math
import random


class dataFactoryInterface(object):

    def __init__(self):
        self.__name = 'dataFactoryInterface'

    def create(self, target):
        classname = target + 'Sampling'
        return eval(classname)()


class DataFactory(object):

    def __init__(self):
        self.__name = 'dataFactory'

    def sampling(self, **kwargs):
        raise Exception("This is a base factory")


class IntSampling(DataFactory):

    def __init__(self):
        super().__init__()
        self.__name = 'iniSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        return result


class FloatSampling(DataFactory):

    def __init__(self):
        super().__init__()
        self.__name = 'floatSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.uniform(next(it), next(it))
            result.append(tmp)
        return result


class BoolSampling(DataFactory):

    def __init__(self):
        super().__init__()
        self.__name = 'boolSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.getrandbits(1)
            result.append(tmp)
        return result


class selfDefinedClassSampling(DataFactory):

    def __init__(self):
        super().__init__()
        self.__name = 'selfDefinedClassSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result


class GetMatrix():
    def __init__(self):
        self.__name = 'GetMatrix'

    def get_all(self, *args):
        int_list = args[0].get('Int')
        float_list = args[0].get('Float')
        bool_list = args[0].get('Bool')
        num = args[0].get('num')
        tp, fp, tn, fn = 0, 0, 0, 0
        for i in range(0, num):
            if bool_list[i] == 1:
                if int_list[i] <= float_list[i]:
                    tp = tp + 1
                else:
                    fp = fp + 1
            else:
                if int_list[i] <= float_list[i]:
                    tn = tn + 1
                else:
                    fn = fn + 1
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
        return str(mcc), str(acc)


@Decorator
def pred(*args, **kwargs):
    print(args, **kwargs)


if __name__ == '__main__':
    name_list = ['Int', 'Float', 'Bool']
    value_dic = {}
    interface = dataFactoryInterface()
    paras = {'datarange': (0, 10), 'num': 10}
    value_dic['num'] = paras.get('num')

    for name in name_list:
        obj = interface.create(name)
        result = obj.sampling(**paras)
        value_dic[name] = result
    mcc, acc = pred(value_dic)
    print('pred:acc:' + acc, 'mcc:' + mcc)