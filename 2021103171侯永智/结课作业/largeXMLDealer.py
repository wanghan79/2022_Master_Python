
"""
  Author:  H.Wang --<>
  Purpose: To parse the large XML files more than 500M
  Created: 4/4/2016
"""

from lxml import etree
from os import path
from optparse import OptionParser
import time


def dealwithElementdfsbuildtree1(elem,faterDict):
    """"""
    if isinstance(elem, object):
        # print(elem)
        faterDict['child'] = []
        if len(elem):
            i = 0
            for child in elem:
                faterDict['child'].append({"root": child.tag})
                if len(child):
                    dealwithElementdfsbuildtree1(child,faterDict['child'][i])
                i=i+1

class largeXMLDealer:
    """
    """

    def __init__(self, fileName):
        self.fileName = fileName
        ns = self._getNamespace(fileName)
        self.ns = "{%s}" % ns


    def __call__(self,func):
        def warpper(*args, **kwargs):
            start = time.time()
            ret = self.parse(self.fileName,func,*args)
            print(f'运行时间:{time.time() - start}')
            return ret
        return warpper


    def parse(self, fileName, func4Element=None,*args):
        """"""
        if not path.isfile(fileName) or not fileName.endswith("xml"):
            raise FileNotFoundError

        count=0
        newargs = []
        tree = {}
        if 	len(self.ns)!=0 and len(args)!=0:
            for x in args:
                newargs.append(self.ns+x)
            print(newargs)
        else:
            newargs=args


        context = etree.iterparse(fileName, events=["start"], tag=newargs)

        for event, elem in context:

            chs = list(elem)
            try:
                if func4Element is not None:
                    tree['root'] = elem.tag
                    func4Element(elem,tree)
                    print(tree)
            except Exception:
                raise Exception("Something wrong in function parameter: func4Element")
            finally:
                elem.clear()
                count = count + 1
                while elem.getprevious() is not None:
                    del elem.getparent()[0]
        del context
        return count


    def _getNamespace(self, fileName):
        """"""
        if not path.isfile(fileName) or not fileName.endswith("xml"):
            raise FileNotFoundError
        result = ''
        es = ('start-ns',)
        context = etree.iterparse(fileName, events=es)
        for event, elem in context:
            prefix, result = elem
            break
        del context
        return result

def main():
    """
    
    """
    # Construct the usage.
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-p", "--print", dest="bPrint", default=False, action="store_true",
                      help="Print results on the screen.")
    parser.add_option("-o", "--output", type="string", dest="outputFile", default=None,
                      help="Output the results to a file.")
    parser.add_option("-t", "--tag", type="string", dest="tag", default="",
                      help="The XML tag interested to parse.")

    (options, args) = parser.parse_args()

    if (len(args) != 1):
        parser.error("You have not input the XML file name")

    filePath = path.normpath(args[0])
    if not path.isfile(filePath) or not filePath.endswith("xml"):
        raise Exception("The input file is not exist or a available XML file.")
    largXML = largeXMLDealer()
    count = largXML.parse(filePath, options.tag)
    print("Parsed %10d XML elements." % count)


def dealwithElementdfsbuildtreelocal(elem,faterDict):
    """"""
    if isinstance(elem, object):
        # print(elem)
        faterDict['child'] = []
        if len(elem):
            # 判断是否有子节点
            i = 0
            for child in elem:
                faterDict['child'].append({"root": child.tag})
                if len(child):
                    dealwithElementdfsbuildtreelocal(child,faterDict['child'][i])
                i=i+1

if __name__ == "__main__":
    largeXMLDealer.parse( largeXMLDealer("P00734.xml"),"P00734.xml" ,dealwithElementdfsbuildtreelocal,"authorList")
