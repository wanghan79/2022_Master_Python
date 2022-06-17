import random


class dataFactoryInterface(object):

    def __init__(self):
        self.__name = 'dataFactoryInterface'

    def create(self, target):
        classname = target + 'Sampling'
        return eval(classname)()


class dataFactory(object):

    def __init__(self):
        self.__name = 'dataFactory'

    def sampling(self, **kwargs):
        raise Exception("This is a base factory")


class intSampling(dataFactory):

    def __init__(self):
        self.__name = 'initSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        return result


class strString(dataFactory):

    def __init__(self):
        self.__name = 'strSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get('strlen')))
            result.append(tmp)
        return result


class selfDefinedStructSampling(dataFactory):

    def __init__(self):
        self.__name = 'selfDefinedStructSampling'

    def sampling(self, **kwargs):
        result = list()
        for index in range(0, kwargs.get('num')):
            element = list()
            for key, value in kwargs.get('struct').items():
                if key == 'int':
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == 'float':
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == 'str':
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value('len')))
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result


class selfDefinedClassSampling(dataFactory):

    def __init__(self):
        self.__name = 'selfDefinedClassSampling'

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
            result.append(tmp)
        return result


if __name__ == '__main__':
    interface = dataFactoryInterface()

    obj = interface.create('int')
    paras = {'datarange': (0, 10), 'num': 3}
    result = obj.sampling(**paras)
    for item in result:
        print(item)