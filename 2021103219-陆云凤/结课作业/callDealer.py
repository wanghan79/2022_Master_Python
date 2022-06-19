#!/usr/bin/env python
# coding:utf-8

from largeXMLDealer import *


def dealwithElement(elem):
    if isinstance(elem, object):
        for child in elem:
            if isinstance(child, object):
                child_list.append(dealwithElement(child))
        if child_list == []:
            dict_elem['child'] = None
        else:
            dict_elem['child'] = child_list
    return dict_elem

def DealerRun(*args, **kwargs):
    print('run')


if __name__ == "__main__":
    fileName = './P00734.xml'
    elemTag = 'accession'
    DealerRun(fileName, elemTag, dealwithElement)