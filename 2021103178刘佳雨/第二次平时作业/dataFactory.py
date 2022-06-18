class dataFactory(object):
    """
   工厂父类
    """
    def __init__(self):
        self.__name = "dataFactory"

    def sampling(self, **kwargs):
        raise "This is a base factory, no implement to sample data!"