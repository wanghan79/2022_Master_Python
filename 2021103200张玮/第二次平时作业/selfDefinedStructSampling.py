import random
import string
from dataFactory import dataFactory



class selfDefinedStructSampling(dataFactory):
    """
    DESCRIPTION:
    """

    def __init__(self):
        self.__name = "selfDefinedStructSampling"

    def sampling(self, **kwargs):
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