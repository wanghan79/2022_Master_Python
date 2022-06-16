from int_sampling import IntSampling
from str_sampling import StrSampling
from self_defined_class_sampling import SelfDefinedClassSampling
from self_defined_struct_sampling import SelfDefinedStructSampling


class DataFactoryInterface(object):
    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()
