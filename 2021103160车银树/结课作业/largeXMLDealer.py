#!/usr/bin/env python
# coding:utf-8
"""
  Author:  H.Wang --<>
  Purpose: To parse the large XML files more than 500M
  Created: 4/4/2016
"""
from optparse import OptionParser
from os import path

from lxml import etree


class largeXMLDealer(object):
    """
    
    """

    def __init__(self, fileName):
        """Constructor"""
        self.fileName = fileName

    def __call__(self, func):
        def warpper(*args, **kwargs):
            count = self.parse(self.fileName, func, *args)
            return count
        return warpper

    def parse(self, fileName, func4Element=None, *elemTag):
        if func4Element is None:
            raise ValueError("func4Element不能为空")
        """"""
        if not path.isfile(fileName) or not fileName.endswith("xml"):
            raise FileNotFoundError

        count = 0
        es = ('end',)
        ns = self._getNamespace(fileName)
        ns = "{%s}" % ns
        tree = {}
        tags = str(elemTag[0]).split(",")
        for tag in tags:
            context = etree.iterparse(fileName, events=["start"], tag=ns + tag)
            for event, elem in context:
                chs = list(elem)
                try:
                    if func4Element is not None:
                        tree['root'] = elem.tag
                        func4Element(elem, tree)
                        print(tree)
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
# Linux Command Line Example:
# python3 largeXMLDealer-1.py -t entry /home/Biodata/OrignalData/Protein/Uniprot/current/uniprot_sprot.xml
