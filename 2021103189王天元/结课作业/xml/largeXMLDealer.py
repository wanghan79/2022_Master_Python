
"""
create by wty
2022/6/2
"""

from lxml import etree
from os import path
from optparse import OptionParser


class largeXMLDealer():
    """

    """

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('largeXMLDealer')
        count = self.parse(*args, **kwargs)
        print("Already parsed %d XML elements." % count)

    # def parse(self, fileName, elemTag, func4Element=None):
    def parse(self, *args, **kwargs):
        """"""
        if not path.isfile(args[0]) or not args[0].endswith("xml"):
            raise FileNotFoundError

        count = 0
        es = ('end',)
        ns = self._getNamespace(args[0])

        ns = "{%s}" % ns
        if args[1] != '':
            tag = ns + args[1]
        else:
            tag = ns + 'uniprot'
        context = etree.iterparse(args[0], events=('start',), tag=tag)

        for event, elem in context:
            # Call the outside function to deal with the element here
            chs = list(elem)
            try:
                if args[2] == None:
                    print('none')
                else:
                    print(args[2](elem))
            except Exception:
                raise Exception("Something wrong in function parameter: func4Element")
            finally:
                elem.clear()
                count = count + 1
                while elem.getprevious() is not None:
                    del elem.getparent()[0]
        del context
        # Return how many elements had been parsed
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
            # print("%s, %d"%(elem, len(elem)))
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

    # Parse the options and args input by users.
    (options, args) = parser.parse_args()

    # Check the correction of users input and call the functions of class DoSomething.
    if (len(args) != 1):
        parser.error("You have not input the XML file name")

    filePath = path.normpath(args[0])
    if not path.isfile(filePath) or not filePath.endswith("xml"):
        raise Exception("The input file is not exist or a available XML file.")
    # Call XML parser
    largXML = largeXMLDealer()
    count = largXML.parse(filePath, options.tag)
    print("Parsed %10d XML elements." % count)


if __name__ == "__main__":
    main()