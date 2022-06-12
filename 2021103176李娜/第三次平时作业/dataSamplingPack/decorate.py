import string
from dataFactoryInterface import dataFactoryInterface
from selfDefinedStructSampling import selfDefinedStructSampling

if __name__ == '__main__':
    interface = dataFactoryInterface()
    # 生成自定义结构随机数
    obj = interface.create("selfDefinedStruct")
    paras = {"num": 5, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 10000)}, "bool": "",
                                  "str": {"datarange": string.ascii_uppercase, "len": 50}}}
    # 任意参数装饰器
    # result = obj.sampling(**paras)
    # 位置参数装饰器
    result = obj.sampling(paras)

    # 打印输出
    print(result)
