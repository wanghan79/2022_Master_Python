



class dataFactoryInterface(object):
    def __init__(self):
        self.name = "dataFactoryInterface"

    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()
