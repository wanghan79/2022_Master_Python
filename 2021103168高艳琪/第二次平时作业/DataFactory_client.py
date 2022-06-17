import string
from DataFactoryInterface import dataFactoryInterface
#该py文件为客户端
#通过访问类工厂接口，实现生产各类数据

if __name__ == "__main__":
    interface = dataFactoryInterface()

    #生产整型数据
    obj_int = interface.create("int")
    paras_int = {"datarange":(0,10),"num":5}
    # 包裹参数传递的实现是在定义函数时在形参前面加上*或**，
    # *所对应的形参会被解释为一个元组(tuple)，而**所对应的形参会被解释为一个字典。
    result_int = obj_int.sampling(**paras_int)
    print('输出随机生成的整数：')
    for item_int in result_int:
        print(item_int,end=' ')
    print()
    print("=========================")
    #生产字符串类型数据
    obj_str = interface.create("str")
    paras_str = {"datarange":string.ascii_uppercase,"num":5,"strlen":8}
    result_str = obj_str.sampling(**paras_str)
    print('输出随机生成的字符串：')
    for item_str in result_str:
        print(item_str,end=' ')
    print()
    print("=========================")

    #生成多类型数据列表
    obj_structure = interface.create("selfDefinedStruct")
    paras_structure = {"num":5,"struct":{"int":{"datarange":(0,100)},"float":{"datarange":(0,10000)},"str":{"datarange":string.ascii_uppercase,"len":50}}}
    result_structure = obj_structure.sampling(**paras_structure)
    print("输出多类型数据列表")
    for item_structure in result_structure:
        print(item_structure)
    print("=========================")
    #创建num个新的类对象
    obj_class = interface.create("selfDefinedClass")
    paras_class = {"num":5,"classname":"Myclass","parameters":5}
    result_class = obj_class.sampling(**paras_class)
    print("输出新的类对象")
    for item_class in result_class:
        print(item_class)
