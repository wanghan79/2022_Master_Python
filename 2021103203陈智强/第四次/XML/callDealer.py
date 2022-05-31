#!/usr/bin/env python
# coding:utf-8

from largeXMLDealer import *



@largeXMLDealer(fileName="test.xml")
def dealwithElementdfsbuildtree(elem,faterDict):
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
                    dealwithElementdfsbuildtree1(child,faterDict['child'][i])
                i=i+1

@largeXMLDealer(fileName="test.xml")
def dealwithElementbfsbuildtree(elem,faterDict):
    """"""
    if isinstance(elem, object):
        # print(elem)
        faterDict['child'] = []
        if len(elem):
            # 判断是否有子节点
            i = 0
            for child in elem:
                faterDict['child'].append({"root": child.tag})
                i=i+1
            i = 0
            for child in elem:
                if len(child):
                    dealwithElementdfsbuildtree1(child, faterDict['child'][i])
                i = i + 1

def dealwithElementdfsbuildtree1(elem,faterDict):
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
                    dealwithElementdfsbuildtree1(child,faterDict['child'][i])
                i=i+1

if __name__ == "__main__":
    dealwithElementdfsbuildtree()
    dealwithElementbfsbuildtree()
    # 或
    # dealwithElementdfsbuildtree('level-1')
    # 用装饰类执行

    # tree={}
    # with open('test.xml', 'rb') as xml:
    #     for event, element in etree.iterparse(xml, events=["start"]):
    #         tree['root']=element.tag
    #         dealwithElementdfsbuildtree1(element, tree)
    #         print(tree)
    # 直接执行
