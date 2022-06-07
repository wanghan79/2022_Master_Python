import random
from dataFactory import dataFactory


class intSampling(dataFactory):
    """
    DESCRIPTION
    整数随机生成
    """

    def __init__(self):
        self.__name = "intSampling"

    def sampling(self, **kwargs):
        result = list()
        try:
            assert ('num' in kwargs.keys() and 'datarange' in kwargs.keys()), \
                "The input dictionary should contain 'num' and 'datarange'"
            for _ in range(0, kwargs.get('num')):
                it = iter(kwargs.get('datarange'))
                tmp = random.randint(next(it), next(it))
                result.append(tmp)
        except BaseException as e:
            print(e)
        return result
