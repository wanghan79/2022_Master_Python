import string

from dataFactoryInterface import dataFactoryInterface

if __name__ == "__main__":
    interface = dataFactoryInterface()

    # Sampling int
    obj=interface.create("int")
    parser = {"datarange":(0,30),"num":5}
    result = obj.sampling(**parser)
    for item in result:
        print(item)

    #Sampling str
    obj = interface.create("str")
    parser = {"datarange": string.ascii_uppercase, "num": 100,"strlen":50}
    result = obj.sampling(**parser)
    for item in result:
        print(item)

    #Sampling self defined structure
    obj = interface.create("selfDefinedStruct")
    paras = {"num":5,"struct":{"int":{"datarange":(0,100)},"float":{"datarange":(0,10000)},"str":{"datarange":string.ascii_uppercase,"strlen":50}}}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    # Sampling self defined class
    obj=interface.create("selfDefinedClass")
    parser = {"num":5,"classname":"MyClass","parameters":5}
    result = obj.sampling(**parser)
    for item in result:
        print(item)