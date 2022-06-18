import random
from dataFactory import DataFactory


class SelfDefinedStructSampling(DataFactory):
    def __init__(self):
        super().__init__()
        self.__name = "selfDefinedStructSampling"

    def sampling(self, **kwargs):
        if 'num' not in kwargs.keys() or 'struct' not in kwargs.keys():
            print("Error in params, please check it again")
            return
        result = list()
        for index in range(0, kwargs.get('num')):
            element = list()
            for key, value in kwargs.get("struct").items():
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == "float":
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == "str":
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result
