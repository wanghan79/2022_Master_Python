import random

import datafactory


class selfDefinedClassSampling(datafactory.dataFatory):
    """
    生成自定义类的随机数
    """

    def __init__(self):
        self.__name = "selfDefinedClassSampling"

    def sampling(self, **kwargs):
        result = list()
        if ('num' or 'classname' or 'prarmeters') not in kwargs:
            result.append("err")
            result.append("parameter not right,please input again")
            return result
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result

class MyClass(object):
    def __init__(self,index):
        pass


