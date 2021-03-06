import string

from dataFactoryInterface import DataFactoryInterface



if __name__ == '__main__':
    interface = DataFactoryInterface()
    # Sampling int
    obj_int = interface.create("Int")
    param = {"datarange": (0, 10), "num": 5}
    result = obj_int.sampling(**param)
    for item in result:
        print(item)

    # Sampling str
    obj_str = interface.create("Str")
    param = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    result = obj_str.sampling(**param)
    for item in result:
        print(item)

    #Sampling self defined structure
    obj = interface.create("SelfDefinedStruct")
    param = {"struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 10000)},
                        "str": {"datarange": string.ascii_uppercase, "len": 8}}, "num": 5}
    result = obj.sampling(**param)
    for item in result:
        print(item)

    #Sampling self defined class
    obj = interface.create("SelfDefinedClass")
    param = {"num": 5, "classname": "MyClass", "parameters": 5}
    result = obj.sampling(**param)
    for item in result:
        print(item)
