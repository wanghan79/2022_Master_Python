#!/usr/bin/env python
# coding:utf-8

import sys

from 结课作业.largeXMLDealer import largeXMLDealer


@largeXMLDealer(fileName="./P00734.xml")
def dealwithElement(elem, xmlDict):
    if isinstance(elem, object):
        xmlDict['child'] = []
        if len(elem):
            i = 0
            for child in elem:
                xmlDict['child'].append({"root": child.tag})
                i = i + 1
            i = 0
            for child in elem:
                if len(child):
                    dealwithElement(child, xmlDict['child'][i])
                i = i + 1


def dealwithElementTree(elem, xmlDict):
    """"""

    if isinstance(elem, object):
        xmlDict['child'] = []
        if len(elem):
            i = 0
            for child in elem:
                xmlDict['child'].append({"root": child.tag})
                i = i + 1
            i = 0
            for child in elem:
                if len(child):
                    dealwithElementTree(child, xmlDict['child'][i])
                i = i + 1


#  无elemTag的入参  entry
#  多elemTag的入参  entry,source
#  单elemTag的入参  source
if __name__ == "__main__":
    if len(sys.argv) == 2:
        elemTag = sys.argv[1]
    elif len(sys.argv) == 1:
        elemTag = 'entry'
    count = dealwithElement(elemTag)
    print("Already parsed %d XML elements." % count)
