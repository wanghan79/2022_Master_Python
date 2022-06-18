import random

"""
实现生成对应类型Sampling对象的接口
"""
class dataFactoryInterface(object):

    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()

"""
声明sampling方法的父类
"""
class dataFactory(object):

    def __init__(self):
        self.__name = "dataFactory"

    def sampling(self, **kwargs):
        raise "This is a base factory, no implement to sample data!"


"""
实现自定义结构sampling的类
"""
class selfDefinedStructSampling(dataFactory):

    def __init__(self):
        self.__name = "selfDefinedStructSampling"

    def sampling(self, **kwargs):
        result = list()
        for index in range(0, kwargs.get('num')):
            element = list()
            for key, value in kwargs.get("struct").items():
                if key == 'int':
                    it = iter(value['dataRange'])
                    tmp = random.randint(next(it), next(it))
                elif key == 'float':
                    it = iter(value['dataRange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == 'bool':
                    tmp = random.getrandbits(1) # 返回具有指定位数的整数
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result

