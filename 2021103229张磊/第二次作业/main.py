import string

from dataFactoryInterface import dataFactoryInterface

if __name__ == "__main__":
    interface = dataFactoryInterface()

    # Sampling int
    obj = interface.create("int")
    paras = {"datarange": (0, 10), "num": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    #Sample str
    obj = interface.create("str")
    paras = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    #Sample self defined structure
    obj = interface.create("selfDefinedStruct")
    paras = {"num": 5, "struct": {"int": {"datarange": (0, 10)}, "float": {"datarange": (0, 10)}, "str": {"datarange": string.ascii_uppercase, "len": 20}}}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    obj = interface.create("selfDefinedClass")
    paras = {"num": 5, "classname": "MyClass", "parameters": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)
