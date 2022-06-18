
class MyClass(object):
    classVar = 456

    def __init__(self,index):
        self.memVar = index;
        self.memlist = list()

        def memberFunction(self): # 固定，可变，默认，关键字
            print("This is a member function in MyClass.")

        def __privateFunction(self):
            print("This is a 'private' function in MyClass.")

        def __copy__(self):
            print("This is a inherate function in MyClass.")

        def __str__(self):
            return "MyClass"