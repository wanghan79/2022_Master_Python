
from intSampling import intSampling
from floatSampling import floatSampling
from boolSampling import boolSampling

class dataFactoryInterface(object):
    def __init__(self):
        self.__name = "dataFactoryInterface"
    
    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()