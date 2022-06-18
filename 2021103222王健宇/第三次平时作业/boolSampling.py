
from selfSamping import *

class boolSampling(dataFactory):

    def __init__(self):
        self.__name = "boolSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('dataRange'))
            tmp = random.getrandbits(1)
            result.append(tmp)
        return result