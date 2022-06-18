#!/usr/bin/env python
# coding:utf-8

import sys
from largeXMLDealer import *

@largeXMLDealer(fileName="P00734.xml")

def dealwithElement(elem,fileDict):

    if isinstance(elem, object):
        fileDict['child'] = []
        if len(elem):
            i = 0
            for child in elem:
                fileDict['child'].append({"root": child.tag})
                i=i+1
            i = 0
            for child in elem:
                if len(child):
                    dealwithElementtree(child, fileDict['child'][i])
                i = i + 1

def dealwithElementtree(elem,fileDict):
    """"""

    if isinstance(elem, object):
        fileDict['child'] = []
        if len(elem):
            i = 0
            for child in elem:
                fileDict['child'].append({"root": child.tag})
                i=i+1
            i = 0
            for child in elem:
                if len(child):
                    dealwithElementtree(child, fileDict['child'][i])
                i = i + 1

if __name__ == "__main__":
    dealwithElement()

