from intFactory import IntSampling
from strFactory import StrSampling
from SelfDefinedClassFactory import SelfDefinedClassSampling
from SelfDefinedStructFactory import SelfDefinedStructSampling

class DataFactoryInterface(object):
    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()
