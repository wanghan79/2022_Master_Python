import random
import string
from dataFactory import *
from main import *

class selfDefinedClassSampling(dataFactory):
    """
    DESCRIPTION:
    """

    def __init__(self):
        self.__name = "selfDefinedClassSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result