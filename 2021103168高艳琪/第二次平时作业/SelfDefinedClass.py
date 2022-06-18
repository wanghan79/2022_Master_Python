from DataFactory import dataFactory
from Myclass import Myclass
class selfDefinedClassCreate(dataFactory):
    """
    通过该文件访问自定义类
    """
    def __int__(self):
        self.__name = "strDefinedClassCreate"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0,kwargs.get('num')):
            #访问自定义类型的类，
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result