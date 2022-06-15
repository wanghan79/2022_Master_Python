import string
import datafactoryinterface
if __name__ == '__main__':
    interface = datafactoryinterface.dataFactoryInterface()
    #生成整型随机数
    # obj = interface.create("int")
    # paras = {"datarange": (0,10), "num": 5}
    # result = obj.sampling(**paras)


    # 生成字符串随机数
    # obj = interface.create("str")
    # paras = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    # result = obj.sampling(**paras)

    # 生成自定义结构随机数
    obj = interface.create("selfDefinedStruct")
    paras = {"num": 5, "struct":{"int": {"datarange": (0,100)}, "float": {"datarange": (0,10000)}, "bool": "", "str": {"datarange": string.ascii_uppercase,  "len": 50}}}
    result = obj.sampling(**paras)

    # 生成自定义类随机数
    # obj = interface.create("selfDefinedClass")
    # paras = {"num": 5, "classname": "MyClass", "parameters": 5}
    # result = obj.sampling(**paras)

    #打印输出
    if result[0] == "err":
        print(result[1])
    else:
        for item in result:
            print(item)

