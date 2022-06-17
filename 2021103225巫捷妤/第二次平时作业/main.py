from dataFactory import dataFactory
from dataFactoryInterface import dataFactoryInterface
from intSampling import intSampling
from strSampling import strSampling
from selfDefinedClassSampling import selfDefinedClassSampling
from selfDefinedStructSampling import selfDefinedStructSampling
import string
import MyClass

if __name__ == "__main__":
    interface = dataFactoryInterface()


    # Sampling int
    obj = interface.create('int')
    paras = {"datarange": (0, 10), "num": 5}
    #result = obj.sampling(**paras)
    result = intSampling().sampling(**paras)
    for item in result:
        print(item)


    # # Sampling str
    # obj = interface.create("str")
    # paras = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    # result = strSampling().sampling(**paras)
    # for item in result:
    #     print(item)



    # # Sampling self defined structure
    # obj = interface.create("selfDefinedStruct")
    # paras = {"num": 5, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 10000)}, "str": {"datarange": string.ascii_uppercase, "len": 50}}}
    # result = selfDefinedStructSampling().sampling(**paras)
    # for item in result:
    #     print(item)


    # obj = interface.create("selfDefinedClass")
    # paras = {"num": 5, "classname": "MyClass", "paramters": 5}
    # result = selfDefinedClassSampling().sampling(**paras)
    # for item in result:
    #     print(item)
