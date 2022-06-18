
from hw2.dataFactory import dataFactory
from hw2.intSampling import intSampling
from hw2.MyClass import MyClass
import string
from hw2.dataFactoryInterface import dataFactoryInterface
if __name__ == "__main__":
    interface = dataFactoryInterface()
    #int
    obj = interface.create("int")
    paras = {"datarange": (0, 10), "num": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)
    #str
    obj = interface.create("str")
    paras = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    #  self defined structure
    obj = interface.create("selfDefinedStruct")
    paras = {"num": 5, "struct":{"int":{"datarange": (0,100)}, "float": {"datarange": (0,10000)}, "str": { "datarange": string.ascii_uppercase, "strlen": 8}}}
    result = obj.sampling(**paras)
    for item in result:
        print(item)
    # defined class structure
    obj = interface.create("selfDefinedClass")
    paras = {"num": 5, "classname": "MyClass", "paramenters": 58}
    result = obj.sampling(**paras)
    for item in result:
        print(item)
