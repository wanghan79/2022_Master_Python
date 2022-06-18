import random

from dataFactory import dataFactory


class selfDefinedStructSampling(dataFactory):
    def __init__(self):
        self.__name = "selfDefinedStructSampling"

    def sampling(self,**kwargs):
        result = list()
        if not isinstance(kwargs.get('num'),int):  # 判断是否为整型数字
            raise Exception("num必须为整型数字")

        for index in range(0,kwargs.get("num")):
            element = list()
            for key,value in kwargs.get("struct").items():
                if key == "int":
                    if not isinstance(value['datarange'][0], int):  # 判断是否为整型数字
                        raise Exception("随机数范围必须为整型数字")
                    if not isinstance(value['datarange'][1], int):  # 判断是否为整型数字
                        raise Exception("随机数范围必须为整型数字")
                    it=iter(value['datarange'])
                    tmp=random.randint(next(it),next(it))
                elif key == "float":
                    if not isinstance(value['datarange'][0], int):  # 判断是否为整型数字
                        raise Exception("随机数范围必须为整型数字")
                    if not isinstance(value['datarange'][1], int):  # 判断是否为整型数字
                        raise Exception("随机数范围必须为整型数字")
                    it=iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key=="str":
                    if not isinstance(value['datarange'], str):
                        raise Exception("随机数范围必须为字符串")
                    if not isinstance(value['strlen'], int):  # 判断是否为整型数字
                        raise Exception("长度必须为整型数字")
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen']))
                elif key == "bool":
                    tmp = random.randint(0,1)
                elif key == "lable":
                    tmp = random.randint(0,1)
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result
