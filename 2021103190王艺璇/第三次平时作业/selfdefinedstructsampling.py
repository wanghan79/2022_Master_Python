import random
from functools import wraps
from math import sqrt

import datafactory




def calculate_data(TP, FP, FN, TN):
    numerator = (TP * TN) - (FP * FN)  # 马修斯相关系数公式分子部分
    denominator = sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))  # 马修斯相关系数公式分母部分
    result = numerator / denominator
    return result


class selfDefinedStructSampling(datafactory.dataFatory):


    def __init__(self):
        self.__name = "selfDefinedsStructSampling"

    """
        定义sampling的装饰函数（计算精度，任意参数）
    """
    # def ACC(decPara):
    #     def decorator(func):
    #         @wraps(func)
    #         def wrapper(*args, **kwargs):
    #             #计算精度
    #             result = func(*args, **kwargs)
    #             sum = 0
    #             count = 0
    #             for item in result:
    #                 sum += 1
    #                 if item[2] == 1:
    #                     count += 1
    #             return count/sum
    #         return wrapper
    #     return decorator
    """
            定义sampling的装饰函数（计算精度，位置参数）
    """
    # def ACC(decPara):
    #     def decorator(func):
    #         @wraps(func)
    #         def wrapper(self, struct):
    #             #计算精度
    #             result = func(self, struct)
    #             sum = 0
    #             count = 0
    #             for item in result:
    #                 sum += 1
    #                 if item[2] == 1:
    #                     count += 1
    #             return count/sum
    #         return wrapper
    #     return decorator



    """
        定义sampling的装饰函数（计算马修斯，任意参数）
    """

    def MCC(decPara):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # 计算马修斯精度
                result = func(*args, **kwargs)
                TP = 0
                TN = 0
                FP = 0
                FN = 0
                for item in result:
                    if item[2] == 1:
                        TP += 1
                    else:
                        TN += 1
                return calculate_data(TP, FP, FN, TN)
            return wrapper
        return decorator

    """
           定义sampling的装饰函数（计算马修斯，位置参数）
    """

    # def MCC(decPara):
    #     def decorator(func):
    #         @wraps(func)
    #         def wrapper(self,struct):
    #             # 计算马修斯精度
    #             result = func(self,struct)
    #             TP = 0
    #             TN = 0
    #             FP = 0
    #             FN = 0
    #             for item in result:
    #                 if item[2] == 1:
    #                     TP += 1
    #                 else:
    #                     TN += 1
    #             return calculate_data(TP, TN, FP, FN)
    #         return wrapper
    #
    #     return decorator

    """
        生成随机数，任意参数
    """

    # @ACC("decPara")
    # @MCC("decPara")
    # def sampling(self, **kwargs):
    #     result = list()
    #     if ('num' or 'struct') not in kwargs:
    #         result.append("err")
    #         result.append("parameter not right,please input again")
    #         return result
    #     for index in range(0, kwargs.get('num')):
    #         element = list()
    #         for key,value in kwargs.get('struct').items():
    #             if key == 'int':
    #                 it = iter(value['datarange'])
    #                 tmp = random.randint(next(it),next(it))
    #             elif key == 'float':
    #                 it = iter(value['datarange'])
    #                 tmp = random.uniform(next(it),next(it))
    #             elif key == 'str':
    #                 it = iter(value['datarange'])
    #                 tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
    #             elif key == 'bool':
    #                 tmp = random.randrange(0, 2, 1)
    #             else:
    #                 break
    #             element.append(tmp)
    #         result.append(element)
    #     return result

    """
           生成随机数，位置参数
    """
    # @ACC("decPara")
    @MCC("decPara")
    def sampling(self, struct):
        result = list()
        if ('num' or 'struct') not in struct:
            result.append("err")
            result.append("parameter not right,please input again")
            return result
        for index in range(0, struct.get('num')):
            element = list()
            for key, value in struct.get('struct').items():
                if key == 'int':
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == 'float':
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == 'str':
                    it = iter(value['datarange'])
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                elif key == 'bool':
                    tmp = random.randrange(0, 2, 1)
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result






