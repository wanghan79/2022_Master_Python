import string

import m1
if __name__=="__main__":
    interface=m1.dataFactoryInterface()
    obj = interface.create("selfDefinedClass")
    paras={"num":5,"classname":"MyClass"}
    result=obj.sampling(**paras)
    for item in result:
        print(item)