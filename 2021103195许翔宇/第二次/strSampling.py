import random

from dataFactory import dataFactory


class strSampling(dataFactory):
    def __init__(self):
        self.__name = "strSampling"



    def sampling(self,**kwargs):
        result = list()

        if not isinstance(kwargs.get('num'),int):  # 判断是否为整型数字
            raise Exception("num必须为整型数字")
        if not isinstance(kwargs.get('datarange'),str):
            raise Exception("随机数范围必须为字符串")
        if not isinstance(kwargs.get('strlen'),int):  # 判断是否为整型数字
            raise Exception("长度必须为整型数字")

        for _ in range(0,kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get("strlen")))
            result.append(tmp)
        return 
