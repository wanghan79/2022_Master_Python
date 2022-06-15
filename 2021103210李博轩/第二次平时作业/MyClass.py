class TestClass():
    pass

class MyClass(object):

    classVar = 456

    def __init__(self, index):
        self.memVar = index
        self.memList = list()

    def memberFunction(self):
        print("member")

    def __privateFunction(self):
        print("private")

    def __copy__(self):
        print("inherate")

    def __str__(self):
        return "MyClass"

    def __del__(self):
        pass

    def __eq__(self, other):
        pass