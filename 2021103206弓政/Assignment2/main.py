import string
from dataFactoryInterface import dataFactoryInterface

if __name__ == "__main__":
    interface = dataFactoryInterface()

    # Sampling int
    obj = interface.create("int")
    paras = {"datarange": (0, 10), "num": 5}
    result = obj.sampling(**paras)
    print(result)
    for item in result:
         print(item)

    # # Sampling str
    # obj = interface.create("str")
    # paras = {"datarange": string.ascii_uppercase, "num": 10, "strlen": 50}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)
    #
    # # Samplnig self defined structure
    # obj = interface.create("selfDefinedStruct")
    # paras = {"num": 10, "struct":{"int":{"datarange": (0, 100)},  "float": {"datarange": (0, 10000)}, "str": {"datarange": string.ascii_uppercase, "len": 50}}}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)
    #
    # # Samplnig self defined class
    # obj = interface.create("selfDefinedClass")
    # paras = {"classname": "MyClass", "num": 5, "parameters": 5}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)