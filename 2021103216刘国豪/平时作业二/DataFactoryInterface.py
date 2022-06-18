from intSampling import *
from StrSampling import *
from SelfDefinedStructSampling import *
from SelfDefinedClassSampling import *

class dataFactoryInterface(object):
    def __init__(self):
        self.__name="dataFactoryInterface"

    def create(self,target):
        classname=target+"Sampling"
        return eval(classname)()