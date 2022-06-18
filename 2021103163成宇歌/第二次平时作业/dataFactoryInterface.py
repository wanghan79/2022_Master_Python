import random
from m3 import intSampling
from m4 import strSampling
from m5 import selfDefinedStructSampling
from m6 import selfDefinedClassSampling
class dataFactoryInterface(object):
    def __init__(self):
        self.__name="dataFactoryInterface"
    def create(self,target):
        classname = target + "Sampling"
        return eval(classname)()



