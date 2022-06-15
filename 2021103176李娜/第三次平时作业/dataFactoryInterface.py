from intSampling import intSampling
from strSampling import strSampling
from selfDefinedStructSampling import selfDefinedStructSampling
from selfDefinedClassSampling import selfDefinedClassSampling


# 对外的模块接口，创造类工厂
class dataFactoryInterface(object):
    """
    DESCRIPTION:工厂接口类。create动态创建所需要的类的实体,实例化合成的类
    """

    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()
