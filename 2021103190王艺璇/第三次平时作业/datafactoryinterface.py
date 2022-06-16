import intsampling
import strsampling
import selfdefinedclasssampling
import selfdefinedstructsampling

class dataFactoryInterface(object):

    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self,target):
        name = ""
        if target == "int":
            name = "intsampling."
        elif target == "str":
            name = "strsampling."
        elif target == "selfDefinedClass":
            name = "selfdefinedclasssampling."
        elif target == "selfDefinedStruct":
            name = "selfdefinedstructsampling."
        else:
            return
        classname = name+target + "Sampling"
        return eval(classname)()
