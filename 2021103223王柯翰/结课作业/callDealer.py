from largeXMLDealer import *


@largeXMLDealer(fileName="sourceFile.xml")
def dealwithElementbfsbuildtree(element, sourceDict):

    if isinstance(element, object):
        sourceDict['child'] = []
        if len(element):
            i = 0
            for child in element:
                sourceDict['child'].append({"root": child.tag})
                i = i+1
            i = 0
            for child in element:
                if len(child):
                    dealwithElementdfsbuildtreeAnother(
                        child, sourceDict['child'][i])
                i = i + 1


def dealwithElementdfsbuildtreeAnother(element, sourceDict):
    """"""

    if isinstance(element, object):
        sourceDict['child'] = []
        if len(element):
            i = 0
            for child in element:
                sourceDict['child'].append({"root": child.tag})
                i = i+1
            i = 0
            for child in element:
                if len(child):
                    dealwithElementdfsbuildtreeAnother(
                        child, sourceDict['child'][i])
                i = i + 1


if __name__ == "__main__":
    dealwithElementbfsbuildtree()
