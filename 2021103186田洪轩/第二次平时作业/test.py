import string
from dataFactoryInterface import dataFactoryInterface


if __name__ == "__main__":
    interface = dataFactoryInterface()

    print("Test Case for Int Sampling.")
    obj = interface.create("int")
    paras = {"datarange" : (8, 18), "num" : 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    print("Test Case for String Sampling.")
    obj = interface.create("str")
    paras = {"datarange" : string.ascii_uppercase, "num": 5, "strlen":8}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    print("Test Case for self defined struct Sampling.")
    obj = interface.create("selfDefinedStruct")
    paras = {"num":5, "struct": {"int": {"datarange":(0,100)},"float":{"datarange":(0,10000)},"str":{"datarange":string.ascii_uppercase,"len":50}}}
    result = obj.sampling(**paras)
    for item in result:
        print(item)


    print("Test Case for self defined class Sampling.")
    obj = interface.create("selfDefinedClass")
    paras = {"num":5, "classname": "MyClass", "parameters":5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)