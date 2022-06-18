import random

from dataFactory import dataFactory


class selfDefineStructSampling(dataFactory):
    """
    自定义结构的随机数生成
    """
    def __init__(self):
        self.__name = "selfDefineStructSampling"

    def sampling(self,**kwargs):
        result = list()
        if ('num' or 'struct') not in kwargs:
            result.append("err")
            result.append("parameter not right,please input again")
            return result

        for index in range(0,kwargs.get('num')):
            element = list()
            for key,value in kwargs.get('struct').items():
                if key == "int":
                    it = iter(value['dataRange'])
                    tmp = random.randint(next(it),next(it))
                elif key == "float":
                    it = iter(value['dataRange'])
                    tmp = random.uniform(next(it),next(it))
                elif key == "str":
                    tmp = ''.join(random.SystemRandom().choice(value['dataRange']) for _ in range(value['len']))
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result

