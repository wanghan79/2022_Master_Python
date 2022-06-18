
from largeXMLDealer import *

@largeXMLDealer(fileName="P00734.xml")
def Tree_element(elem,faterDict):

    if isinstance(elem, object):
        faterDict['child'] = []
        if len(elem):
            i = 0
            for child in elem:
                faterDict['child'].append({"root": child.tag})
                i=i+1
            i = 0
            for child in elem:
                if len(child):
                    Tree_element1(child, faterDict['child'][i])
                i = i + 1

def Tree_element1(elem,faterDict):
    """"""

    if isinstance(elem, object):
        faterDict['child'] = []
        if len(elem):
            i = 0
            for child in elem:
                faterDict['child'].append({"root": child.tag})
                i=i+1
            i = 0
            for child in elem:
                if len(child):
                    Tree_element1(child, faterDict['child'][i])
                i = i + 1

if __name__ == "__main__":
    Tree_element()

