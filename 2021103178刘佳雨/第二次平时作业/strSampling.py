import random
import string
from dataFactory import dataFactory


class strSampling(dataFactory):
    """
   字符串随机数生成
    """
    def __init__(self):
        self.__name = "strSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get('strlen')))
            result.append(tmp)
        return result

if __name__ == "__main__":
    from dataFactoryInterface import dataFactoryInterface

    interface = dataFactoryInterface()

    #Sampling str
    obj = interface.create("str")
    paras = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    result = obj.sampling(**paras)
    for item in result:
        print(item)