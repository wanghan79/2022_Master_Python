import random
from dataFactory import dataFactory

class floatSampling(dataFactory):

    def __init__(self):
        self.__name = 'floatSampling'

    def sampling(self, **kwargs):
        result = list()
        try:
            for _ in range(0, kwargs.get('num')):
                it = iter(kwargs.get('datarange'))
                tmp = random.uniform(next(it), next(it))
                result.append(tmp)
        except:
            print("Argument Error.Example:{\"datarange\" : (8, 18), \"num\" : 5}")
        return result