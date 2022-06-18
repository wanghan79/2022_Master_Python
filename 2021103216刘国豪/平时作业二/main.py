import string
from DataFactoryInterface import dataFactoryInterface

#随机生成int型
if __name__=="__main__":
    interface = dataFactoryInterface()
    obj = interface.create("int")
    paras = {"datarange": (0, 10), "num": 5}
    result = obj.Sampling(**paras)
    for item in result:
        print(item)


#随机生成长度为8的字符串
    obj = interface.create("Str")
    paras = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    result = obj.Sampling(**paras)
    for item in result:
        print(item)

# 随机生成[int,float,string]的列表
    obj = interface.create("SelfDefinedStruct")
    paras = {"num": 5, "struct": {"int": {"datarange": (0, 10)}, "float": {"datarange": (0, 10)}, "str": {"datarange": string.ascii_uppercase, "len": 20},"bool":{"datarange": (0, 1)}}}
    result = obj.Sampling(**paras)
    for item in result:
        print(item)
#随机生成自定义类
    obj = interface.create("SelfDefinedClass")
    paras = {"num": 5, "classname": "MyClass", "parameters": 5}
    result = obj.Sampling(**paras)
    for item in result:
        print(item)

