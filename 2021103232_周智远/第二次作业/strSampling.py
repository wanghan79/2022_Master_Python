import random
from dataFactory import dataFactory

class strSampling(dataFactory):

    def __init__(self):
        self.__name = 'strSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get('strlen')))
            result.append(tmp)
        return result