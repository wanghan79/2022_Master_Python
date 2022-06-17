from INT import intSampling
from STR import strSampling
from SDSS import selfDefinedStructSampling
from SDCS import selfDefinedClassSampling

class dataFactoryInterface(object):

    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self, target):
        classname = target + "Sampling"

        return eval(classname)()