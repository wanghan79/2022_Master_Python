import random

from dataFactory import dataFactory


class intSampling(dataFactory):
    def __init__(self):
        self.__name = "intSampling"

    def sampling(self,**kwargs):
        result = list()
        """
        考虑添加代码保护：
        如果调用者传入的kwargs不满足生成整数的两个键值，num和dataRange不符合要求（不是合法输入）
        则返回给调用者一个提示信息
        """
        if ('num' or 'dataRange') not in kwargs:
            result.append("err")
            result.append("parameter not right,please input again")
            return result
        for _ in range(0,kwargs.get('num')):
            it = iter(kwargs.get('dataRange'))
            tmp = random.randint(next(it),next(it))
            result.append(tmp)
        return result

