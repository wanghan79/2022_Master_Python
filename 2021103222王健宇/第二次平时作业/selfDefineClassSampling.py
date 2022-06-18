from dataFactory import dataFactory



class selfDefineClassSampling(dataFactory):
    """
    自定义类的随机生成
    """
    def __init__(self):
        self.__name = "selfDefineClassSampling"

    def sampling(self,**kwargs):
        result = list()
        if ('num' or 'className' or 'parameters') not in kwargs:
            result.append("err")
            result.append("parameter not right,please input again")
            return result
        for _ in range(0,kwargs.get('num')):
            tmp = eval(kwargs.get('className'))(kwargs.get('parameter'))
            result.append(tmp)
        return result


class MyClass(object):

    def __init__(self, index):
        self.res = list()
        self.res.append(str(index))
        print(self.res)
