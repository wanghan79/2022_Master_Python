from DataFactory import dataFactory
import random
class intCreate(dataFactory):
    """
    该类为生成随机整数的类，继承于dataFactory
    个数为：num
    范围为：datarange
    """
    def __int__(self):
        self.__name="intCreate"

    def sampling(self,**kwargs):
        result = list()
        for _ in range(0,kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            temp = random.randint(next(it),next(it))
            result.append(temp)
        return result
