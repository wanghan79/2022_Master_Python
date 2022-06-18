import random
from dataFactory import dataFactory
# import dataFactory

class SelfDefinedStructSampling(dataFactory):
    def __init__(self):
        self.__name="SelfDefinedStructSampling"

    def Sampling(self, **kwargs):
        result = list()
        if not isinstance(kwargs.get('num'),int):
            raise Exception("num必须为整数")
        for index in range(0, kwargs.get('num')):
            element=list()
            for key,value in kwargs.get("struct").items():
                if key=="int":
                    # 取值范围datarange的上限、下限必须为整数
                    if isinstance(value['datarange'][0], int)&isinstance(value['datarange'][1], int):
                        it=iter(value['datarange'])
                        tmp=random.randint(next(it),next(it))
                    else:
                        raise Exception("随机数范围必须为整型数字")
                elif key=="float":
                    # 取值范围datarange的上限、下限必须为数字、非字符
                    if not (isinstance(value['datarange'][0], str) & isinstance(value['datarange'][1], str)):
                        it = iter(value['datarange'])
                        tmp = random.uniform(next(it), next(it))
                    else:
                        raise Exception("随机数范围必须为数字")
                elif key=="str":
                    tmp=''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                elif key=="bool":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it),next(it))
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result