import random

import datafactory


class selfDefinedStructSampling(datafactory.dataFatory):


    def __init__(self):
        self.__name = "selfDefinedsStructSampling"

    def sampling(self, **kwargs):
        result = list()
        if ('num' or 'struct') not in kwargs:
            result.append("err")
            result.append("parameter not right,please input again")
            return result
        for index in range(0, kwargs.get('num')):
            element = list()
            for key,value in kwargs.get('struct').items():
                if key == 'int':
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it),next(it))
                elif key == 'float':
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it),next(it))
                elif key == 'str':
                    it = iter(value['datarange'])
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result


