class dataFactory(object):
    def __init__(self):
        self.__name="dataFactory"

    def Sampling(self,**kwargs):
        raise "this is a base factory,no implement to sample data"#这是一个基类，子类在外部