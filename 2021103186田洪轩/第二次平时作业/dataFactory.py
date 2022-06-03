import random
import string
# 接口放在一个文件
# 基类放在一个文件
# 四个实现放在四个文件
# 再写一个测试文件
# 异常处理

class dataFactory(object):
    def __init__(self):
        self.__name = "dataFactory"
    
    def sampling(self, **kwargs):
        raise "This is a base factory."

