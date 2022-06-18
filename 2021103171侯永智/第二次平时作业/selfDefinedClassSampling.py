from dataFactory import dataFactory
from Demo import Demo


class selfDefinedClassSampling(dataFactory):

    def __int__(self):
        self.__name = "selfDefinedClassSampling"

    def sampling(self, **kwargs):
        result = list()
        print(kwargs.get('classname'))
        print(kwargs.get('parameters'))
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result
