from intFactory import intSampling
from floatFactory import floatSampling
from boolFactory import  boolSampling
from selfDefinedClassFactory import selfDefinedClassSampling

class dataFactoryInterface(object):

    def __init__(self):
        self.__name = 'dataFactoryInterface'

    def create(self, target):
        classname = target + 'Sampling'
        return eval(classname)()

