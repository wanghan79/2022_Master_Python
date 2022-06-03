
from intSampling import intSampling
from strSampling import strSampling
from selfDefinedClassSampling import selfDefinedClassSampling
from selfDefinedStructSampling import selfDefinedStructSampling


class dataFactoryInterface(object):
    def __init__(self):
        self.__name = "dataFactoryInterface"
    
    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()