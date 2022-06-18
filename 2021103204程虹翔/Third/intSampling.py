import random
from dataFactory import DataFactory


class IntSampling(DataFactory):
    def __init__(self):
        super().__init__()
        self.__name = "intSampling"

    def sampling(self, **kwargs):
        result = list()
        if 'num' not in kwargs.keys() or 'datarange' not in kwargs.keys():
            print("Error in params, please check it again")
            return
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        return result
