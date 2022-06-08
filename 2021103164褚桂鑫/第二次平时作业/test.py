import string

from 第二次平时作业.dataFactoryInterface import dataFactoryInterface

# 测试几种类型
if __name__ == '__main__':
    print('*'*15+'测试创建类类型'+'*'*15)
    item = {'num': 10, 'datarange': (1, 10)}
    interface = dataFactoryInterface()
    create = interface.create("int")
    res = create.sampling(**item)
    print(res)

    print('\n'+'*'*10+'测试创建类类型'+'*'*10)
    paras = {'num': 10, 'datarange': string.ascii_uppercase, 'strlen': 10}
    interface = dataFactoryInterface()
    create = interface.create("str")
    res = create.sampling(**paras)
    for item in res:
        print(item)

    print('\n'+'*'*15+'测试创建类类型'+'*'*15)

    paras = {'num': 5, 'struct': {"int": {'datarange': [0, 100]}, 'float': {"datarange": [0, 1000]},
                                  "str": {'datarange': string.ascii_uppercase, 'strlen': 10}}}
    interface = dataFactoryInterface()
    create = interface.create("selfDefinedStruct")
    res = create.sampling(**paras)
    for item in res:
        print(item)

    print('\n'+'*'*18+'测试创建类类型'+'*'*18)
    paras = {"num": 5, "classname": "MyClass", "parameters": 5}
    interface = dataFactoryInterface()
    create = interface.create("selfDefinedClass")
    res = create.sampling(**paras)
    for item in res:
        print(item)