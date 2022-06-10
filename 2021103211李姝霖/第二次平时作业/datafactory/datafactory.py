#整数随机数生成

#字符串随机数生成

#小数随机数生成

from intSampling import intSampling
from strSampling import strSampling
from selfDefinedStructSampling import selfDefinedStructSampling
from selfDefinedClassSampling import selfDefinedClassSampling
from MyClass import MyClass
import string
import random


class dfInterface(object):
    """
      对外接口
    """
    def __init__(self):
        self.name = dfInterface
    def create(self,target):
        #合成类名
        classname = target + "Sampling"
        return eval(classname)()

class df(object):
    """
        父类
    """
    def __init__(self):
        self.name = "df"
    def sampling(self,**kwargs):
        return "datafactory"






if __name__ == "__main__":
    interface = dfInterface()

    #Sampling int
    obj = interface.create("int")
    paras = {"datarange":(0,10),"num":5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    # Sampling str
    obj = interface.create("str")
    paras = {"datarange": string.ascii_uppercase, "num": 5,"strlen":8}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    # Sampling self defined structure
    obj = interface.create("selfDefinedStruct")
    paras = {"num":5,"struct":{"int":{"datarange":(0,100)},
                               "float":{"datarange":(0,10000)},
                               "str":{"datarange": string.ascii_uppercase, "len":50}}}
    result = obj.sampling(**paras)
    for item in result:
        print(item)


    # Sampling self class structure
    obj = interface.create("selfDefinedClass")
    paras = {"num":5, "classname":'MyClass',"parameters":5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)
