
import random

from dataFactoryInterface import dataFactoryInterface
from dataFactory import dataFactory

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
        raise Exception("This is a base factory,no implement to sample data")


class intSampling(dataFactory):

    def __init__(self):
        self.__name = 'initSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it), next(it))
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

if __name__ == '__main__':
    interface = dataFactoryInterface()

    obj = interface.create('int')
    paras = {'datarange': (0, 10), 'num': 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)