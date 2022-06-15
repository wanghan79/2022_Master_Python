from dataFactoryInterface import dataFactoryInterface
import string

if __name__ == "__main__":

    interface = dataFactoryInterface()

    obj = interface.create("int")
    paras = {"datarange": (0, 10), "num": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

