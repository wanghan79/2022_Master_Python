from dataFactoryInterface import dataFactoryInterface
import string

# 测试
# 定义主函数入口，能被os直接调用
if __name__ == "__main__":
    # 创建接口实例，后续执行相应的动作
    interface = dataFactoryInterface()

    # Sampling int
    obj = interface.create("int")
    paras = {"datarange": (0, 10), "num": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)

    # Sampling str
    # obj = interface.create("str")
    # paras = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)

    # Sampling self defined structure
    # obj = interface.create("selfDefinedStruct")
    # paras = {"num": 5, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 1000)},
    #                               "str": {"datarange": string.ascii_uppercase, "len": 50}}}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)

    # Sampling self defined class
    # obj = interface.create("selfDefinedClass")
    # paras = {"num": 5, "classname": "MyClass", "parameters": 5}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)
