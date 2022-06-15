from dataFactory import dataFactory
from MyClass import MyClass


class selfDefinedClassSampling(dataFactory):
    """
    DESCRIPTION:自定义类的随机数生成
    """

    def __init__(self):
        self.__name = "selfDefinedClassSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            # classname需要在当前py文件能看到
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result
