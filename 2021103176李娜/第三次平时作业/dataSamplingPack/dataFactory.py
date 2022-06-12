class dataFactory(object):
    """
    DESCRIPTION:工厂类。给外部看到的，类工厂的父类/基类
    """

    def __init__(self):
        self.__name = "dataFactory"

    def sampling(self, **kwargs):
        raise "This is a base factory, no implement to sample data!"
