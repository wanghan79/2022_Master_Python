#!/usr/bin/env python
# coding:utf-8
from largeXMLDealer import *

@largeXMLDealer(filename)
def dealwithElementbfsbuildtree(elem,Dict):

    if isinstance(elem, object):
        Dict['child'] = []
        if len(elem):
            i = 0
            for child in elem:
                Dict['child'].append({"root": child.tag})
                i=i+1
            i = 0
            for child in elem:
                if len(child):
                    dealwithElementbfsbuildtree1(child, Dict['child'][i])

                i = i + 1

def dealwithElementbfsbuildtree1(elem,Dict):
    """"""
    if isinstance(elem, object):
        Dict['child'] = []
        if len(elem):
            i = 0
            for child in elem:
                Dict['child'].append({"root": child.tag})
                if len(child):
                    dealwithElementdfsbuildtree(child, Dict['child'][i])
                i = i + 1

if __name__ == "__main__":
    dealwithElementbfsbuildtree()

