from DataFactory import dataFactory
import random
from Myclass import Myclass


class selfDefinedClassSampling(dataFactory):
    """

    """

    def __init__(self):
        self.__name = "strDefinedClassSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0,kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result