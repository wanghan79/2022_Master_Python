import random
from dataFactory import dataFactory


class intSampling(dataFactory):
    """
    整型随机数生成
    """
    def __init__(self):
        self.__name = "intSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        return result

if __name__ == "__main__":
    from dataFactoryInterface import dataFactoryInterface

    interface = dataFactoryInterface()  #如果导入dataFactoryInterface，会引起循环引用问题

    #Sampling int
    obj = interface.create("int")
    paras = {"datarange": (0, 10), "num": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)