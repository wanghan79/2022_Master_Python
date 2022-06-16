import selfdefinedstructsampling
import string
import datafactoryinterface
if __name__ == '__main__':
    interface = datafactoryinterface.dataFactoryInterface()
    # 生成自定义结构随机数
    obj = interface.create("selfDefinedStruct")
    paras = {"num": 5, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 10000)}, "bool": "",
                                  "str": {"datarange": string.ascii_uppercase, "len": 50}}}
    #调用任意参数装饰器
    # result = obj.sampling(**paras)
    # 调用位置参数装饰器
    result = obj.sampling(paras)

    print(result)