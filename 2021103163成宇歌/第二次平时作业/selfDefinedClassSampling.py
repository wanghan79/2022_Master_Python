import random
from MyClass import MyClass
from m2 import dataFactory
class selfDefinedClassSampling(dataFactory):
    def __init__(self):
        self.__name="selfDefinedClassSampling"
    def sampling(self,**kwargs):
        result = list()
        for _ in range(0,kwargs.get('num')):
            tmp=eval(kwargs.get('classname'))()
            result.append(tmp)
        return result