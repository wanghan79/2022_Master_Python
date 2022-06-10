import string

from dataFactoryInterface import dataFactoryInterface

if __name__ == '__main__':
    interface = dataFactoryInterface()

    # # Sampling int
    # obj = interface.create("int")
    # paras = {'datarange': (0, 100), 'num': 5}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)


    # # Sampling str
    # obj = interface.create("str")
    # paras = {"datarange": string.ascii_uppercase, "num": 3, "strlen": 5}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)

    # # Sampling self defined structure
    # obj = interface.create("selfDefinedStruct")
    # paras = {"num": 5, "struct": {"int": {"datarange": (0,100)}, "float": {"datarange": (0,1000)}, "ste": {"datarange": string.ascii_uppercase}, "len": 50}}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)

    # Sampling selfDefinedClass
    obj = interface.create("selfDefinedClass")
    paras = {"num": 5, "classname": "MyClass", "parameters": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)
