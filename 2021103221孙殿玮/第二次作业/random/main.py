import string

from dataFactoryInterface import dataFactoryInterface

if __name__ == '__main__':
    interface=dataFactoryInterface()
    # int
    obj = interface.create("int")
    parser = {"datarange": (0, 10), "num": 5}
    result = obj.sampling(**parser)
    for item in result:
        print(item)

    # str
    obj = interface.create("str")
    parser = {"datarange": string.ascii_uppercase, "num": 50, "strlen": 50}
    result = obj.sampling(**parser)
    for item in result:
        print(item)
