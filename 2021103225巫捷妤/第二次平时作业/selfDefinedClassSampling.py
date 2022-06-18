import dataFactory
import MyClass

class selfDefinedClassSampling(dataFactory.dataFactory):
    def __init__(self):
        self.__name = "selfDefinedClassSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get("num")):
            #tmp = eval(kwargs.get("classname"))(kwargs.get("paramters"))
            tmp = kwargs.get("classname")
            result.append(tmp)
        return result