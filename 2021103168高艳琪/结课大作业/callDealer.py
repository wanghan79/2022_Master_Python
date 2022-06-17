#!/usr/bin/env python
# coding:utf-8
from largeXMLDealer import largeXMLDealer
@largeXMLDealer
def DealerStrat(*args, **kwargs):
    print('start')
if __name__ == "__main__":
    fileName = './P00734.xml'
    elemTag = 'recommendedName'
    DealerStrat(fileName, elemTag)
