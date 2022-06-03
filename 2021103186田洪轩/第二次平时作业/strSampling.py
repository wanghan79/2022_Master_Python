import random
from dataFactory import dataFactory


class strSampling(dataFactory):
    def __init__(self):
        self.__name = "strFactory"
    
    def sampling(self, **kwargs):
        result = list()
        try:
            for _ in range(0, kwargs.get('num')):
                tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get('strlen')))     
                result.append(tmp)
        except:
            print("Argument Error. Example: {\"datarange\" : string.ascii_uppercase, \"num\": 5, \"strlen\":8}")
        return result