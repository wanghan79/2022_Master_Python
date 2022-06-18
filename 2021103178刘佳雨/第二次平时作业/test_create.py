import string

from dataFactoryInterface import dataFactoryInterface

interface = dataFactoryInterface()


# Sampling int
def create_int():
    obj = interface.create("int")
    paras = {"datarange": (0, 10), "num": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

#Sampling str
def create_str():
    obj = interface.create("str")
    paras = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

# Sampling self defined structure
def create_DefinedStruct():
    obj = interface.create("selfDefinedStruct")
    paras = {"num": 5, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 10000)},
                                  "str": {"datarange": string.ascii_uppercase, "len": 50}}}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

# Sampling self defined class
def create_DefinedClass():
    obj = interface.create("selfDefinedClass")
    paras = {"num": 5, "classname": "Coke", "parameters": 3}
    result = obj.sampling(**paras)
    for item in result:
        print(item)


create_int()
