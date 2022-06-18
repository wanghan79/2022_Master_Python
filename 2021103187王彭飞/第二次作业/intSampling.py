import random
from hw2.dataFactory import dataFactory
class intSampling(dataFactory):
    def __init__(self) -> None:
        self.__name = "intSampling"
    def sampling(self, **kwargs):
            kwargs.get('num')
            result = list()
            for _ in range(0, kwargs.get('num')):
                it = iter(kwargs.get('datarange'))
                tmp = random.randint(next(it), next(it))
                result.append(tmp)
            return result