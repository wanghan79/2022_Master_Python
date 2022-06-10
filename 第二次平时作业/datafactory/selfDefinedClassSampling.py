
import random
from MyClass import MyClass

class selfDefinedClassSampling(object):
    """
    类随机数生成
    """
    def __init__(self):
        self._name = "selfDefinedClassSampling"
    def sampling(self,**kwargs):
        result = list()
        for _ in range(0,kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result