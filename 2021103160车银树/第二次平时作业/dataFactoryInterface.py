from intSampling import intSampling
from strSampling import strSampling
from selfDefinedClassSampling import selfDefinedClassSampling
from selfDefinedStructSampling import selfDefinedStructSampling
from boolSampling import boolSampling

class dataFactoryInterface(object):
    def __init__(self):
        self.__name = "data_factory_interface"

    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()
