import string
from dataFactoryInterface import DataFactoryInterface


def sampleInt(interface):
    obj = interface.create("Int")
    paras = {"datarange": (0, 10), "num": 5}
    result = obj.sampling(**paras)
    if result is not None:
        print(result)
        for item in result:
            print(item)
    else:
        print("Something went wrong, result is empty, please check")


def sampleStr(interface):
    obj = interface.create("Str")
    paras = {"datarange": string.ascii_uppercase, "num": 10, "strlen": 50}
    result = obj.sampling(**paras)
    if result is not None:
        print(result)
        for item in result:
            print(item)
    else:
        print("Something went wrong, result is empty, please check")


def sampleSelfDefinedClass(interface):
    obj = interface.create("SelfDefinedClass")
    paras = {"classname": "MyClass", "num": 5, "parameters": 5}
    result = obj.sampling(**paras)
    if result is not None:
        print(result)
        for item in result:
            print(item)
    else:
        print("Something went wrong, result is empty, please check")


def sampleSelfDefinedStructure(interface):
    obj = interface.create("SelfDefinedStruct")
    paras = {"num": 10, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 10000)},
                                   "str": {"datarange": string.ascii_uppercase, "len": 50}}}
    result = obj.sampling(**paras)
    if result is not None:
        print(result)
        for item in result:
            print(item)
    else:
        print("Something went wrong, result is empty, please check")


if __name__ == "__main__":
    interface = DataFactoryInterface()
    sampleSelfDefinedStructure(interface)



