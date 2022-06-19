import random
import string
from dataFactory import dataFactory

from selfDefinedStructSampling import *

class intSampling(dataFactory):
    """
    DESCRIPTION:
    """

    def __init__(self):
        self.__name = "intSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it),next(it))
            result.append(tmp)
        return result

