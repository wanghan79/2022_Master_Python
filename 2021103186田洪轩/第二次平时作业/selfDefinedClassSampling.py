from dataFactory import dataFactory
from MyClass import MyClass

class selfDefinedClassSampling(dataFactory):
    def __init__(self):
        self.__name = "selfDefinedClassSampling"

    def sampling(self, **kwargs):
        result = list()
        try:
            for _ in range(0, kwargs.get('num')):
                tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
                result.append(tmp)
        except NameError:
            print("Class Not Found.")
        except:
            print("Bad Input. Please check your Input.")
        return result