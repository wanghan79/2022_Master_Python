import random

from dataFactory import dataFactory


class strSampling(dataFactory):
    def __init__(self):
        self.__name = "strSampling"


    def sampling(self,**kwargs):
        result = list()
        """
        代码保护，num dataRange strLen的合法输入，不符合则提醒调用者
        """
        if ('strLen' or 'dataRange') not in kwargs:
            result.append("err")
            result.append("parameter not right,please input again")
            return result

        for _ in range(0,kwargs.get('num')):
            tmp = ''.join(random.SystemRandom().choice(kwargs.get('dataRange'))for _ in range(kwargs.get('strLen')))
            result.append(tmp)
        return result
