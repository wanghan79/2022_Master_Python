class dataFactory(object):

    def __init__(self):
        self.__name = 'dataFactory'

    def sampling(self, **kwargs):
        raise Exception("This is a base factory")