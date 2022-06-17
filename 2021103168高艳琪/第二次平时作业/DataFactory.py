class dataFactory(object):
    """
    这是一个工厂类
    其他生产数据的类都要继承该类
    """
    def __init__(self):
        self.__name="dataFactory"
    def sampling(self,**kwargs):
        raise "生产数据请通过接口进行调用"