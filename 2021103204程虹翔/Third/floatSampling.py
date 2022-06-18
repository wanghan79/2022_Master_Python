import random
from dataFactory import DataFactory


class FloatSampling(DataFactory):
    def __init__(self):
        super().__init__()
        self.__name = 'floatSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.uniform(next(it), next(it))
            result.append(tmp)
        return result
