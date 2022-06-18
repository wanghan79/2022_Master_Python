
class dataFactory(object):
    """
    只作为一个基准的父类，不用按照外部需求负责生成子类
    """
    def __init__(self):
        self.__name = "dataFactory"

    def sampling(self,**kwargs): # 传入不定长的键值对,能够灵活接受各种输入
        raise "This is a base factory, no implement to sample data!"

