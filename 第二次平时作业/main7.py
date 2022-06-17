import m1
if __name__=="__main__":
    interface=m1.dataFactoryInterface()
    obj = interface.create("int")
    paras={"datarange":(0,10),"num":5}
    result=obj.sampling(**paras)
    for item in result:
        print(item)