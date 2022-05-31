#!/usr/bin/env python
# coding:utf-8

from largeXMLDealer import *



@largeXMLDealer(fileName="test.xml")
def dealwithElementdfsbuildtree(elem,faterDict):
    if isinstance(elem, object):
        faterDict['child'] = []
        # 用列表存子树
        # len(elem)判断是否有子节点
        for index in range(len(elem)):
            faterDict['child'].append({"root": elem[index].tag})
            if len(elem[index]):
                dealwithElementdfsbuildtree1(elem[index],faterDict['child'][index])


def dealwithElementdfsbuildtree1(elem,faterDict):
    """"""
    if isinstance(elem, object):
        faterDict['child'] = []
        for index in range(len(elem)):
            faterDict['child'].append({"root": elem[index].tag})
            if len(elem[index]):
                dealwithElementdfsbuildtree1(elem[index],faterDict['child'][index])

if __name__ == "__main__":
    dealwithElementdfsbuildtree()


