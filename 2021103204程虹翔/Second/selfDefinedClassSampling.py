from dataFactory import DataFactory
from MyClass import MyClass


class SelfDefinedClassSampling(DataFactory):
    def __init__(self):
        super().__init__()
        self.__name = "selfDefinedClassSampling"

    def sampling(self, **kwargs):
        result = list()
        if 'num' not in kwargs.keys() or 'classname' not in kwargs.keys() or 'parameters' not in kwargs.keys():
            print("Error in params, please check it again")
            return
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result
