import string
from DataFactory import dataFactory
from DataFactoryInterface import dataFactoryInterface
from DataFactory import dataFactory
from intSampling import intSampling

if __name__ == "__main__":
    interface = dataFactoryInterface()

    #int_try
    obj_int = interface.create("int")
    paras_int = {"datarange":(0,10),"num":5}
    result_int = obj_int.sampling(**paras_int)
    for item_int in result_int:
        print(item_int)

    #str_try
    obj_str = interface.create("str")
    paras_str = {"datarange":string.ascii_uppercase,"num":5,"strlen":8}
    result_str = obj_str.sampling(**paras_str)
    for item_str in result_str:
        print(item_str)

    #self definde structure try
    obj_structure = interface.create("selfDefinedStruct")
    paras_structure = {"num":5,"struct":{"int":{"datarange":(0,100)},"float":{"datarange":(0,10000)},"str":{"datarange":string.ascii_uppercase,"len":50}}}
    result_structure = obj_structure.sampling(**paras_structure)
    for item_structure in result_structure:
        print(item_structure)

    #self defined class try
    obj_class = interface.create("selfDefinedClass")
    paras_class = {"num":5,"classname":"Myclass","parameters":5}
    result_class = obj_class.sampling(**paras_class)
    for item_class in result_class:
        print(item_class)
