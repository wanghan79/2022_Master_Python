import random

from 第三次平时作业.dataFactory import dataFactory


class strSampling(dataFactory):

    def __int__(self):
        self.__name = "strSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            item = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get('strlen')))
            result.append(item)
        return result
