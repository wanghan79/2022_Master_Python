import random


class dataFactoryInterface(object):

    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()


class dataFactory(object):

    def __init__(self):
        self.__name = "dataFactory"

    def sampling(self, **kwargs):
        raise "This is a base factory, no implement to sample data!"


class selfDefinedStructSampling(dataFactory):

    def __init__(self):
        self.__name = "selfDefinedStructSampling"

    def sampling(self, **kwargs):
        result = list()
        for index in range(0, kwargs.get('num')):
            element = list()
            for key, value in kwargs.get("struct").items():
                if key == 'int':
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == 'float':
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == 'bool':
                    tmp = random.getrandbits(1)

                else:
                    break
                element.append(tmp)
            result.append(element)
        return result


class boolSampling(dataFactory):

    def __init__(self):
        self.__name = "boolSampling"

    def sampling(self, **kwargs):
        result = list()
        for index in range(0, kwargs.get('num')):
            element = list()
            tmp = random.getrandbits(1)
            result.append(tmp)
        return result
