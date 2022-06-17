
class dataFactoryInterface(object):
    def __init__(self):
        self.__name = "dateFactoryInterface"

    def create(self, target):
        classname = "target + 'Sampling'"
        reslut = eval(classname)
        return reslut


