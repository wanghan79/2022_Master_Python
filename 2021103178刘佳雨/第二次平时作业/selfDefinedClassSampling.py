from Coke import Coke
from dataFactory import dataFactory

class selfDefinedClassSampling(dataFactory):
    """
    特定类随机数生成
    """
    def __init__(self):
        self.__name = "selfDefinedClassSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters')).drink()
            result.append(tmp)
        return result


if __name__ == "__main__":
    from dataFactoryInterface import dataFactoryInterface

    interface = dataFactoryInterface()

    # Sampling self defined class
    obj = interface.create("selfDefinedClass")
    paras = {"num": 5, "classname":"Coke", "parameters": 3}
    result = obj.sampling(**paras)
    for item in result:
        print(item)