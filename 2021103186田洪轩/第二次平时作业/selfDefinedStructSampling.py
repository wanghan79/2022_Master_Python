import random

from dataFactory import dataFactory


class selfDefinedStructSampling(dataFactory):
    def __init__(self):
        self.__name = "selfDefinedStructSampling"

    def sampling(self, **kwargs):
        result = list()
        try:
            for index in range(0, kwargs.get('num')):
                element = list()
                for key,value in kwargs.get("struct").items():
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
        except KeyError:
            print("Key Error. Please Check your Key in your struct.")
        except TypeError:
            print("Type Error. Please Check your Type in your struct.")
        except:
            print("Struct Error. Please Check your input.")
        return result