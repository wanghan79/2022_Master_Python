
class MyClass(object):
    def __init__(self, index):
        self.memVar = index
        self.memlist = list()

    def memberFunction(self):
        print("This is a member function in MyClass")

    def __privateFunction(self):
        print("This is a 'private' function in MyClass")

    def __copy__(self):
        print("This is a inherate function in MyClass")
