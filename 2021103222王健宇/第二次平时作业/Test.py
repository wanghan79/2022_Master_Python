import string

from dataFactoryInterface import dataFactoryInterface



if __name__ == '__main__':
     interface = dataFactoryInterface()

     """
     动态Sampling int
     """
     obj = interface.create("int")
     paras = {'dataRange':(0,10),'num':5}
     result = obj.sampling(**paras)


     """
     动态Sampling str
     """
     # obj = interface.create("str")
     # paras = {"dataRange":string.ascii_uppercase,"num":5,"strLen":8}
     # result = obj.sampling(**paras)


     """
     动态Sampling self defined structure
     """
     # obj = interface.create("selfDefineStruct")
     # paras = {"num":5,
     #           "struct":{
     #                "int":{"dataRange":(0,100)},
     #                "float":{"dataRange":(0,10000)},
     #                "str":{"dataRange":string.ascii_uppercase,"len":50}
     #                 }
     #          }
     # result = obj.sampling(**paras)
     #

     """
     动态Sampling self defined class
     """
     # obj = interface.create("selfDefineClass")
     # paras = {"num":5,
     #          "className":"MyClass",
     #          "parameters":5}
     # result = obj.sampling(**paras)




     # 输出
     for item in result:
          print(item)