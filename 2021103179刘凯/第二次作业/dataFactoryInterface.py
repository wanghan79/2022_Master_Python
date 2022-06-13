from intSampling import *
from strSampling import *
from selfDefinedClassSampling import *
from selfDefinedStructSampling import *


class dataFactoryInterface(object):
    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()
