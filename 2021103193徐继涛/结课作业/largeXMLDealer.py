#!/usr/bin/env python
# coding:utf-8
"""
  Author:  H.Wang --<>
  Purpose: To parse the large XML files more than 500M
  Created: 4/4/2016
"""
from lxml import etree
from os import path
from optparse import OptionParser


class largeXMLDealer():
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('largeXMLDealer')
        count = self.parse(*args, **kwargs)
        print("Already parsed %d XML elements." % count)

    def parse(self, *args, **kwargs):
        if not path.isfile(args[0]) or not args[0].endswith("xml"):
            raise FileNotFoundError

        count = 0
        ns = self._getNamespace(args[0])
        ns = "{%s}" % ns
        if args[1] != '':
            tag = ns + args[1]
        else:
            tag = ns + 'uniprot'
        context = etree.iterparse(args[0], events=('start',), tag=tag)

        for event, elem in context:
            if args[2] == None:
                print('none')
            else:
                print(args[2](elem))
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


def use_arg():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-p", "--print", dest="bPrint", default=False, action="store_true",
                      help="Print results on the screen.")
    parser.add_option("-o", "--output", type="string", dest="outputFile", default=None,
                      help="Output the results to a file.")
    parser.add_option("-t", "--tag", type="string", dest="tag", default="",
                      help="The XML tag interested to parse.")
    (options, args) = parser.parse_args()
    return (options, args)


def main():
    (options, args) = use_arg()

    filePath = path.normpath(args[0])
    if not path.isfile(filePath) or not filePath.endswith("xml"):
        raise Exception("The input file is not exist or a available XML file.")
    largXML = largeXMLDealer()
    count = largXML.parse(filePath, options.tag)
    print("Parsed %10d XML elements." % count)

if __name__ == "__main__":
    main()