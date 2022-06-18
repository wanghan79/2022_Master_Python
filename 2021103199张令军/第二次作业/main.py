import string

from dataFactoryInterface import dataFactoryInterface

if __name__ == '__main__':
    interface = dataFactoryInterface()
    obj = interface.create("selfDefinedClass")
    paras = {"num": 5, "classname": "MyClass", "parameters": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)
