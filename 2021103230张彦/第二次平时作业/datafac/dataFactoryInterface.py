from datafac.toolSampling import *


class dataFactoryInterface(object):

    def __init__(self):
        self.__name = 'dataFactoryInterface'

    def create(self, target):
        classname = target + 'Sampling'
        # intSampling
        return eval(classname)()
        # return eval('intSampling.intSampling')()