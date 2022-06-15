import random

import datafactory


class strSampling(datafactory.dataFatory):
    """
    生成字符串随机数
    """

    def __init__(self):
        self.__name = "strSampling"

    def sampling(self, **kwargs):
        result = list()
        if ('strlen' or 'datarange') not in kwargs:
            result.append("err")
            result.append("parameter not right,please input again")
            return result
        for _ in range(0, kwargs.get('num')):
            tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get('strlen')))
            result.append(tmp)
        return result


