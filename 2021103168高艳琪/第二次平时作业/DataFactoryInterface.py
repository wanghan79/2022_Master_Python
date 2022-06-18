from intCreate import intCreate
from strCreate import strCreate
from SelfDefinedClass import selfDefinedClassCreate
from SelfDefinedStruct import selfDefinedStructCreate
class dataFactoryInterface(object):
    """
    类工厂的接口
    通过该类生成访问各个随机数生成类的对象
    之后可以通过
    """
    def __init__(self):
        self.__name="daraFactoryInterface"

    def create(self,target):
        classname = target+'Create'
        return eval(classname)()