from DataFactory import dataFactory
import random
class strCreate(dataFactory):
    """
    该类为生成随机字符串的类，继承于dataFactory
    个数为：num
    范围为：datarange
    长度为：strlen
    """
    def __int__(self):
        self.__name = "strCreate"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tem = ''.join(random.SystemRandom().choice(kwargs.get('datarange'))for _ in range(kwargs.get('strlen')))
            result.append(tem)
        return result