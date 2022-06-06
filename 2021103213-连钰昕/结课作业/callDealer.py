#!/usr/bin/env python
# coding:utf-8

from largeXMLDealer import *

@largeXMLDealer(fileName="P00734.xml")
def dealwithElementbfsbuildtree(elem,faterDict):

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
                    dealwithElementbfsbuildtree1(child, faterDict['child'][i])
                i = i + 1

def dealwithElementbfsbuildtree1(elem,faterDict):
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
                    dealwithElementbfsbuildtree1(child, faterDict['child'][i])
                i = i + 1

if __name__ == "__main__":
    dealwithElementbfsbuildtree()

