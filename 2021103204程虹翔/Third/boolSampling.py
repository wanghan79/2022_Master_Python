import random
from dataFactory import DataFactory


class BoolSampling(DataFactory):
    def __init__(self):
        super().__init__()
        self.__name = 'boolSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.getrandbits(1)
            result.append(tmp)
        return result