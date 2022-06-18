import random

from 第三次平时作业.dataFactory import dataFactory


class selfDefinedStructSampling(dataFactory):

    def __int__(self):
        self.__name = "selfDefinedStructSampling"

    def sampling(self, **kwargs):
        random.seed(1)
        result = list()
        for index in range(0, kwargs.get('num')):
            element = list()
            for key, value in kwargs.get('struct').items():
                if key == 'int':
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == 'float':
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == 'str':
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen']))
                elif key == 'bool':
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                element.append(tmp)
            result.append(element)
        return result
