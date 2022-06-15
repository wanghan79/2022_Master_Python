
class TestClass():
    pass


class MyClass(object):

    classVar = 456

    def __init__(self, index):
        self.memVar = index
        self.memList = list()

    def memberFunction(self):
        print("This is a member function in MyClass")

    def __privateFunction(self):
        print("This is a 'private' function in MyClass")

    def __copy__(self):
        print("This is a inherate function in MyClass")

    def __str__(self):
        return "MyClass"

    def __del__(self):
        pass

    def __eq__(self, other):
        pass