import random
from dataFactory import DataFactory


class StrSampling(DataFactory):
    """
    DESCRIPTION
    字符串随机生成
    """

    def __init__(self):
        super().__init__()
        self.__name = "StrSampling"

    def sampling(self, **kwargs):
        result = list()
        if 'num' not in kwargs.keys() or 'datarange' not in kwargs.keys() or 'strlen' not in kwargs.keys():
            print("Error in params, please check it again")
            return
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get('strlen')))
            result.append(tmp)
        return result
