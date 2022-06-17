import string

import m1
if __name__=="__main__":
    interface=m1.dataFactoryInterface()
    obj = interface.create("selfDefinedStruct")
    paras={"num":5,"struct":{"int":{"datarange":(0,100)},"float":{"datarange":(0,10000)},"str":{"datarange":string.ascii_uppercase,"len":50}}}
    result=obj.sampling(**paras)
    for item in result:
        print(item)