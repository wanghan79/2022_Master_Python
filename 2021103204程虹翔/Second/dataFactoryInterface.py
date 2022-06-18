from intSampling import IntSampling
from stringSampling import StrSampling
from selfDefinedClassSampling import SelfDefinedClassSampling
from selfDefinedStructSampling import SelfDefinedStructSampling


class DataFactoryInterface(object):  # 通过接口创建类工厂
    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()
