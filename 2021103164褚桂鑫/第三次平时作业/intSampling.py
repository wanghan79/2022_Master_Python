import random

from 第三次平时作业.dataFactory import dataFactory


class intSampling(dataFactory):

    def __int__(self):
        self.__name = "intSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        return result
