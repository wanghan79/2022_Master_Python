import random
import string
from dataFactory import *
from dataFactoryInterface import *
from intSampling import *
from strSampling import *
from selfDefinedClassSampling import *
from selfDefinedStructSampling import *
from MyClass import *

if __name__ == "__main__":
    interface = dataFactoryInterface()

    # Sampling int
    # print('int:')
    # obj = interface.create("int")
    # paras = {"datarange":(0,10),"num":5}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)

    # Sampling str
    # print('str:')
    # obj = interface.create("str")
    # paras = {"datarange": string.ascii_uppercase, "nun":100,"strlen":50}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)

    # Sampling self defined structure
    # print('structure:')
    # obj = interface.create("selfDefinedStruct")
    # paras = {"num":5,"struct":{"int":{"datarange":(0,100)},"float":{"datarange":(1,10000)},"str":{"datarange":string.ascii_uppercase,"len":50}}}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)

    # Sampling self defined class
    # print('class:')
    obj = interface.create("selfDefinedClass")
    paras = {"num": 5, "classname": "MyClass", "parameters": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)