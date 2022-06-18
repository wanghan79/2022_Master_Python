from intSampling import intSampling
from strSampling import strSampling
from SelfDefinedClass import selfDefinedClassSampling
from SelfDefinedStruct import selfDefinedStructSampling
class dataFactoryInterface(object):
    """

    """
    def __init__(self):
        self.__name="daraFactoryInterface"

    def create(self,target):
        classname = target+"Sampling"
        return eval(classname)()