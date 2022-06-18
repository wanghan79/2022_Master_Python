
from hw2.dataFactory import dataFactory
from hw2.intSampling import intSampling
from hw2.strSampling import strSampling
from hw2.selfDefindstruct import selfDefinedStructSampling
from hw2.selfDefineClass import selfDefinedClassSampling
from hw2.MyClass import MyClass

class dataFactoryInterface(object):
    def __init__(self):
        self.__name = "dataFactoryInterface"
    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()

