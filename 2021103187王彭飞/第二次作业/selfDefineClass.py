
import random
from hw2.dataFactory import dataFactory
from hw2.MyClass import MyClass
class selfDefinedClassSampling(dataFactory):
    def __init__(self) -> None:
        self.__name = "selfDefinedClassSampling"
    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('paramenters'))
            result.append(tmp)
        return result