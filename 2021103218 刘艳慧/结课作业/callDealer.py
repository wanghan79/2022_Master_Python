
import largeXMLDealer
import sys


@largeXMLDealer.largeXMLDealer()
def dealwithElement(elem):
    """"""
    if isinstance(elem, object):
        # print(True)
        for child in elem:
            print(child)


if __name__ == "__main__":
    # if len(sys.argv) == 2:
    # fileName = sys.argv[1]
    # elemTag = sys.argv[2]
    fileName = 'P00734.xml'
    elemTag = 'authorList'
    print("%s, %s" % (fileName, elemTag))
    lxmld = largeXMLDealer.largeXMLDealer()
    # temp=lxmld._getNamespace(fileName)
    # print(type(temp))
    # print(temp)
    count = lxmld.parse(fileName, elemTag, dealwithElement)
    print("Already parsed %d XML elements." % count)

