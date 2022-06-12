"""
    Author:lina
    Purpose:pass.
    Created:10/4/2022
"""
#该py文件可以被dataFactory识别

class TestClass():
    pass


class MyClass(object):
    """
    DESCRIPTION:生成类
    """
    classVar = 456

    def __init__(self, index):
        self.memVar = index
        self.memList = list()

    def memberFunction(self):#固定，可变，默认，关键字
        print("This is a member function in MyClass")

    def __privateFunction(self):
        print("This is a 'private' function in MyClass")

    def __copy__(self):
        print("This is a inherate function in MyClass")
        # super(MyClass,self).__copy__()

    def __str__(self):
        return "MyClass"
        # super().__str__()

    def __del__(self):
        pass

    def __eq__(self, other):
        pass