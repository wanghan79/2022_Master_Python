import string
from Interface import dataFactoryInterface

def CreateInt():
    if __name__ == "__main__":
        interface = dataFactoryInterface()

        obj = interface.create("int")
        paras = {"datarange": (0, 10), "num": 5}
        result = obj.sampling(**paras)
        for item in result:
            print(item)

def CreateStr():
    if __name__ == "__main__":
        interface = dataFactoryInterface()

        obj = interface.create("str")
        paras = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 10}
        result = obj.sampling(**paras)
        for item in result:
            print(item)

def CreateSelfDefinedStr():
    if __name__ == "__main__":
        interface = dataFactoryInterface()

        obj = interface.create("selfDefinedStruct")
        paras = {"num": 5, "struct": {"int":{"datarange":(0,100)},"float":{"datarange":(0,100)},"str":{"datarange":string.ascii_uppercase,"len":5}}}
        result = obj.sampling(**paras)
        for item in result:
            print(item)

def CreateSelfDefinedClass():
    if __name__ == "__main__":
        interface = dataFactoryInterface()

        obj = interface.create("selfDefinedClass")
        paras = {"num": 5, "classname": "MyClass","parameters":5}
        result = obj.sampling(**paras)
        for item in result:
            print(item)

CreateInt()
CreateStr()
CreateSelfDefinedStr()
CreateSelfDefinedClass()


