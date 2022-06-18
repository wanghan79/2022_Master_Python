
import random

from dataFactory import dataFactory
class StrSampling(dataFactory):
    def __init__(self):
        self.__name="StrSampling"

    def Sampling(self, **kwargs):
        result = list()
        #代码保护伪代码：if(datarang>'A' and datarang<'Z' and strlen<=50):pass else:"随机生成字符串格式错误"
        for _ in range(0, kwargs.get('num')):
            tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get('strlen')))
            result.append(tmp)
        return result