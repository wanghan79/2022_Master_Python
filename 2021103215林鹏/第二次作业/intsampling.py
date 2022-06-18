import random

import datafactory

class intSampling(datafactory.dataFatory):

    def __init__(self):
        self.__name = "intSampling"

    def sampling(self, **kwargs):
        result = list()
        if 'num' or 'datarange' not in kwargs:
            result.append("err")
            result.append("parameter not right,please input again")
            return result
        for _ in range(0,kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it),next(it))
            result.append(tmp)
        return result
                

