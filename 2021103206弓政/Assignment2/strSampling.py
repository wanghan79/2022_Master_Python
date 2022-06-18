import random
from dataFactory import dataFactory


class strSampling(dataFactory):
    """
    DESCRIPTION
    字符串随机生成
    """

    def __init__(self):
        self.__name = "srtSampling"

    def sampling(self, **kwargs):
        result = list()
        try:
            assert ('num' in kwargs.keys() and 'datarange' in kwargs.keys()), \
                "The input dictionary should contain 'num' and 'datarange'"
            for _ in range(0, kwargs.get('num')):
                it = iter(kwargs.get('datarange'))
                tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get('strlen')))
                result.append(tmp)
        except BaseException as e:
            print(e)
        return result
