# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.



#from dataFactory import dataFactory
#from dataFactoryInterface import dataFactoryInterface
from dataFactoryInterface import *

import string
# class dataFactoryInterface(object):
#     def __init__(self):
#         self.__name = "dataFactoryInterface"
#
#     def create(self, target):
#         classname = target + "Sampling"
#         return eval(classname)()

# class dataFactoryInterface(object):
#     def __init__(self):
#         self.__name = "dataFactoryInterface"
#
#     def create(self, target):
#         classname = target + "Sampling"
#         return eval(classname)()

if __name__ == '__main__':

    # Sampling int

    interface = dataFactoryInterface()
    obj_int = interface.create("int")
    paras_int = {"datarange": (0, 10), "num": 5}
    result_int = obj_int.sampling(**paras_int)
    for item_int in result_int:
        print(item_int)

    # Sampling str

    obj_str = interface.create("str")
    paras_str = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    result_str = obj_str.sampling(**paras_str)
    for item_str in result_str:
         print(item_str)

    # Sampling self defined structure

    obj_selfD = interface.create("selfDefinedStruct")
    paras_selfD = {"num": 5, "struct": {"int": {"datarange": (0,100)},"float": {"datarange": (0,100000)}, "str": {"datarange":string.ascii_uppercase,"len": 50}}}
    result_selfD = obj_selfD.sampling(**paras_selfD)
    for item_selfD in result_selfD:
        print(item_selfD)

    # Sampling self defined class

    obj_selfC = interface.create("selfDefinedClass")
    paras_selfC = {"num": 5, "classname": "43"}
    result_selfC = obj_selfC.sampling(**paras_selfC)
    for item_selfC in result_selfC:
        print(item_selfC)

