import random
from dataFactory import dataFactory

class intSampling(dataFactory):

    def __init__(self):
        self.__name = 'initSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        return result