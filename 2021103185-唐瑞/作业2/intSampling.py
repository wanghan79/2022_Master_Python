import random

from dataFactory import dataFactory


class intSampling(dataFactory):
    def __init__(self):
        self.__name = "intSampling"

    def sampling(self,**kwargs):
        result = list()

        if not isinstance(kwargs.get('num'),int):
            raise Exception("num必须为整型数字")
        if not isinstance(kwargs.get('datarange')[0],int):
            raise Exception("随机数范围必须为整型数字")
        if not isinstance(kwargs.get('datarange')[1],int):
            raise Exception("随机数范围必须为整型数字")

        for _ in range(0,kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it),next(it))
            result.append(tmp)
        return result