import string

import m1
if __name__=="__main__":
    interface=m1.dataFactoryInterface()
    obj = interface.create("str")
    paras={"datarange":string.ascii_uppercase,"num":100,"strlen":50}
    result=obj.sampling(**paras)
    for item in result:
        print(item)