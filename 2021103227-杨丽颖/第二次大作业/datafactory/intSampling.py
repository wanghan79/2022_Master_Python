#from datafactory import df

import random

class intSampling(object):
    """
    整数随机数生成
    """
    def __init__(self):
        self._name = "intsampling"
    def sampling(self,**kwargs):
        result = list()
        for _ in range(0,kwargs.get('num')):
            it = iter(kwargs.get('datarange'))
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        return result