
from dataFactory import dataFactory
from Myclass import *

class SelfDefinedClassSampling(dataFactory):
    def __init__(self):
        self.__name="SelfDefinedClassSampling"

    def Sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result