#!/usr/bin/env python
# coding:utf-8

from largeXMLDealer import largeXMLDealer
import sys


def dealwithElement(elem):
    """
    取得标签和标签中的内容，并保存到字典中
    """
    dict_elem = {}
    child_list = []
    if isinstance(elem, object):
        # 使用.tan取得标签名,使用.text取得其中的内容
        dict_elem[elem.tag] = elem.text
        for child in elem:
            if isinstance(child, object):
                child_list.append(dealwithElement(child))
        # 如果列表是空，表明没有子节点
        if not child_list:
            dict_elem['child'] = None
        # 列表不为空时，将子节点列表作为字典的值
        else:
            dict_elem['child'] = child_list
    return dict_elem


# 使用largeXMLDealer类装饰DealerStart函数,便于接收参数
@largeXMLDealer
def DealStart(fileName, dealwithElement, *args):
    pass


if __name__ == "__main__":
    # 使用列表存储需要解析的标签
    elemTag = list()

    # 运行方式一：通过命令行赋值参数,可以参考下行的命令行代码
    # python ./Final_Assignment/callDealer.py ./Final_Assignment/P00734.xml accession lineage
    fileName = sys.argv[1]
    for i in range(len(sys.argv) - 2):
        elemTag.append(sys.argv[i + 2])

    # 运行方式二：当然也可以直接赋值给参数
    # fileName = './P00734.xml'
    # elemTag = ['accession', 'lineage']

    DealStart(fileName, dealwithElement, elemTag)

'''
CALL EXAMPLE 1:
COMMAND LINE: python ./Final_Assignment/callDealer.py ./Final_Assignment/P00734.xml accession lineage
OUTPUT:           
{'{http://uniprot.org/uniprot}accession': 'P00734', 'child': None}
{'{http://uniprot.org/uniprot}accession': 'B2R7F7', 'child': None}
{'{http://uniprot.org/uniprot}accession': 'B4E1A7', 'child': None}
{'{http://uniprot.org/uniprot}accession': 'Q4QZ40', 'child': None}
{'{http://uniprot.org/uniprot}accession': 'Q53H04', 'child': None}
{'{http://uniprot.org/uniprot}accession': 'Q53H06', 'child': None}
{'{http://uniprot.org/uniprot}accession': 'Q69EZ7', 'child': None}
{'{http://uniprot.org/uniprot}accession': 'Q7Z7P3', 'child': None}
{'{http://uniprot.org/uniprot}accession': 'Q9UCA1', 'child': None}
{'{http://uniprot.org/uniprot}lineage': '\n', 'child': [{'{http://uniprot.org/uniprot}taxon': 'Eukaryota', 'child': None}, {'
{http://uniprot.org/uniprot}taxon': 'Metazoa', 'child': None}, {'{http://uniprot.org/uniprot}taxon': 'Chordata', 'child': Non
e}, {'{http://uniprot.org/uniprot}taxon': 'Craniata', 'child': None}, {'{http://uniprot.org/uniprot}taxon': 'Vertebrata', 'ch
ild': None}, {'{http://uniprot.org/uniprot}taxon': 'Euteleostomi', 'child': None}, {'{http://uniprot.org/uniprot}taxon': 'Mam
malia', 'child': None}, {'{http://uniprot.org/uniprot}taxon': 'Eutheria', 'child': None}, {'{http://uniprot.org/uniprot}taxon
': 'Euarchontoglires', 'child': None}, {'{http://uniprot.org/uniprot}taxon': 'Primates', 'child': None}, {'{http://uniprot.or
g/uniprot}taxon': 'Haplorrhini', 'child': None}, {'{http://uniprot.org/uniprot}taxon': 'Catarrhini', 'child': None}, {'{http:
//uniprot.org/uniprot}taxon': 'Hominidae', 'child': None}, {'{http://uniprot.org/uniprot}taxon': 'Homo', 'child': None}]}
Already parsed 10 XML elements.        
'''
