import math
import random


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


class intSampling():

    def __init__(self):
        self.__name = 'intSampling'

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


class ACC_GetMatrix():
    def __init__(self):
        self.__name = 'ACC_GetMatrix'

    def get_all(self, *args):
        int_list = args[0].get('int')
        float_list = args[0].get('float')
        bool_list = args[0].get('bool')
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

class MCC_GetMatrix():
    def __init__(self):
        self.__name = 'MCC_GetMatrix'

    def get_all(self, *args):
        int_list = args[0].get('int')
        float_list = args[0].get('float')
        bool_list = args[0].get('bool')
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


class ACC_Decorator():
    def __init__(self, func):
        self._func1 = func
        self.matrix = ACC_GetMatrix()

    def __call__(self, *args, **kwargs):
        tp, fp, tn, fn = self.matrix.get_all(*args)
        ACC = float((tp + tn) / (tp + tn + fp + fn))
        self._func1(*args, **kwargs)
        # print('MCC:'+str(MCC)+' ACC:'+str(ACC))
        return str(ACC)

class MCC_Decorator():
    def __init__(self, func):
        self._func2 = func
        self.matrix = MCC_GetMatrix()

    def __call__(self, *args, **kwargs):
        tp, fp, tn, fn = self.matrix.get_all(*args)
        MCC = float(tp * tn - fp * fn) / (
            math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))) + float(0.000001)
        self._func2(*args, **kwargs)
        # print('MCC:'+str(MCC)+' ACC:'+str(ACC))
        return str(MCC)


@ACC_Decorator
def pred1(dic):
    print(dic)



@MCC_Decorator
def pred2(*args, **kwargs):
    print(*args, **kwargs)


if __name__ == '__main__':
    name_list = ['int', 'float', 'bool']
    value_dic = {}
    interface = dataFactoryInterface()
    paras = {'datarange': (0, 10), 'num': 5}
    value_dic['num'] = paras.get('num')

    for name in name_list:
        obj = interface.create(name)
        result=obj.sampling(**paras)
        value_dic[name] = result
    ACC = pred1(value_dic)
    MCC = pred2(value_dic)
    print('预测结果1:\nACC:' + ACC, '\nMCC:' + MCC)

    name_list = ['int', 'float', 'bool']
    value_dic = {}
    interface = dataFactoryInterface()
    paras = {'datarange': (0, 10), 'num': 10}
    value_dic['num'] = paras.get('num')

    for name in name_list:
        obj = interface.create(name)
        result = obj.sampling(**paras)
        value_dic[name] = result
    ACC = pred1(value_dic)
    MCC = pred2(value_dic)
    print('预测结果2:\nACC:' + ACC, '\nMCC:' + MCC)