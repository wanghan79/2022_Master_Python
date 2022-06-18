
from intSampling import *
from strSampling import *
from selfDefineStructSampling import *
from selfDefineClassSampling import *

class dataFactoryInterface:
    """
    Description:
    外部调用的接口，传入想要生成什么样的随机数
    """
    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self,target): # target是要生成的随机数类别
        className = target+"Sampling"
        return eval(className)()