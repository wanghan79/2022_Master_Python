import dataFactory
import random

class intSampling(dataFactory.dataFactory):
    def __init__(self):
        self.__name = "intSampling"

    def sampling(self, **kwargs):
        l = (0,10)
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(l)
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        return result


