import random
import string

def dataSampling(datatype, datarange, num, strlen=8):  #固定参数；可变参数 *args；默认参数；关键字参数 **kwargs
    """
    :Description: Generate a given condition random data set.
    :param datatype:
    :param datarange:
    :param num:
    :param strlen:
    :return:
    """
    result = set()
    for index in range(0, num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            result.add(item)
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            result.add(item)
            continue
        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            result.add(item)
            continue
        else:
            continue
    return result
