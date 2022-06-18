#!/usr/bin/env python
# coding:utf-8
from largeXMLDealer import *

@largeXMLDealer(fileName="P00734.xml")
def dealwithElementdfsbuildtree(elem,faterDict):
    """"""
    if isinstance(elem, object):

        faterDict['child'] = []
        if len(elem):
            # 判断是否有子节点
            i = 0
            for child in elem:
                faterDict['child'].append({"root": child.tag})
                if len(child):
                    dealwithElementdfsbuildtree1(child,faterDict['child'][i])
                i=i+1

if __name__ == "__main__":
    dealwithElementdfsbuildtree()
    # dealwithElementbfsbuildtree()

