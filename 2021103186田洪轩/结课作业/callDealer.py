#!/usr/bin/env python
# coding:utf-8

import sys
from largeXMLDealer import largeXMLDealer


def dealwithElement(elem):
    """"""
    dict_elem = {}
    child_list = []
    if isinstance(elem, object):
        dict_elem['tag'] = elem
        for child in elem:
            if isinstance(child, object):
                child_list.append(dealwithElement(child))
        if child_list == []:
            dict_elem['child'] = None
        else:
            dict_elem['child'] = child_list
    return dict_elem

@largeXMLDealer
def dealer(*args, **kwargs):
    pass


if __name__ == "__main__":
    if len(sys.argv) == 3:
        fileName = sys.argv[1]
        elemTag = sys.argv[2]
        print("OK. Arguments given are: ")
        print("%s, %s"%(fileName, elemTag))
    else:
        fileName = "P00734.xml"
        elemTag = "sequence"
        print("Argument error, using default args. ")
        print("Usage: python callDealer.py <filename> <elementTag>")
        print("Example: python callDealer.py P00734.xml accession")
    
    dealer(fileName, elemTag, dealwithElement)

'''
CALL EXAMPLE 1:
COMMAND LINE:     python callDealer.py P00734.xml accession
OUTPUT:           
OK. Arguments given are: 
P00734.xml, accession
{'tag': <Element {http://uniprot.org/uniprot}accession at 0x23280f15980>, 'child': None}
{'tag': <Element {http://uniprot.org/uniprot}accession at 0x23280f17880>, 'child': None}
{'tag': <Element {http://uniprot.org/uniprot}accession at 0x23280f62240>, 'child': None}
{'tag': <Element {http://uniprot.org/uniprot}accession at 0x23280f62280>, 'child': None}
{'tag': <Element {http://uniprot.org/uniprot}accession at 0x23280f622c0>, 'child': None}
{'tag': <Element {http://uniprot.org/uniprot}accession at 0x23280f62340>, 'child': None}
{'tag': <Element {http://uniprot.org/uniprot}accession at 0x23280f62380>, 'child': None}
{'tag': <Element {http://uniprot.org/uniprot}accession at 0x23280f623c0>, 'child': None}
{'tag': <Element {http://uniprot.org/uniprot}accession at 0x23280f62400>, 'child': None}
Already parsed 9 XML elements.       


CALL EXAMPLE 2:
COMMAND LINE:     python callDealer.py P00734.xml protein
OUTPUT:           
OK. Arguments given are: 
P00734.xml, protein
{'tag': <Element {http://uniprot.org/uniprot}protein at 0x28849417880>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}recommendedName at 0x288494622c0>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}fullName at 0x28849462480>, 'child': None}, {'tag': <Element {http://uniprot.org/uniprot}ecNumber at 0x288494624c0>, 'child': None}]}, {'tag': <Element {http://uniprot.org/uniprot}alternativeName at 0x28849462300>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}fullName at 0x28849462540>, 'child': None}]}, {'tag': <Element {http://uniprot.org/uniprot}component at 0x28849462340>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}recommendedName at 0x28849462600>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}fullName at 0x288494626c0>, 'child': None}]}]}, {'tag': <Element {http://uniprot.org/uniprot}component at 0x28849462380>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}recommendedName at 0x28849462740>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}fullName at 0x28849462800>, 'child': None}]}]}, {'tag': <Element {http://uniprot.org/uniprot}component at 0x288494623c0>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}recommendedName at 0x28849462880>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}fullName at 0x28849462940>, 'child': None}]}]}, {'tag': <Element {http://uniprot.org/uniprot}component at 0x28849462400>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}recommendedName at 0x28849462a00>, 'child': [{'tag': <Element {http://uniprot.org/uniprot}fullName at 0x28849462ac0>, 'child': None}]}]}]}
Already parsed 1 XML elements.

CALL EXAMPLE 3: (BAD CALL)
COMMAND LINE:     python callDealer.py
OUTPUT:
Argument error, using default args. 
Usage: python callDealer.py <filename> <elementTag>
Example: python callDealer.py P00734.xml accession
{'tag': <Element {http://uniprot.org/uniprot}sequence at 0x1c74c751f00>, 'child': None}
Already parsed 1 XML elements.
'''


