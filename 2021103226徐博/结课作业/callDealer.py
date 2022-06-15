#!/usr/bin/env python
# coding:utf-8

from largeXMLDealer import largeXMLDealerfun



def dealwithElement(elem):
    """
    解析xml树
    """
    elem = {}
    childrenlist = []
    if isinstance(elem, object):
        elem['tag'] = elem
        for child in elem:
            if isinstance(child, object):
                childrenlist.append(dealwithElement(child))
        if childrenlist == []:
            elem['child'] = None
        else:
            elem['child'] = childrenlist
    return elem

@largeXMLDealerfun
def DealerStrat(*args, **kwargs):
    print('starting。。。')


if __name__ == "__main__":
    # if len(sys.argv) == 2:
    fileName = './P00734.xml'
    elemTag = 'protein'
    DealerStrat(fileName, elemTag, dealwithElement)
    # fileName = sys.argv[1]
    # elemTag = sys.argv[2]
    #
    # print("%s, %s"%(fileName, elemTag))
    # lxmld = largeXMLDealer.largeXMLDealer()
    # count = lxmld.parse(fileName, elemTag, dealwithElement)
    # print("Already parsed %d XML elements." % count)

'''
CALL EXAMPLE 1:
COMMAND LINE:     python3 callDealer.py P00734.xml accession
OUTPUT:           
P00734
B2R7F7
B4E1A7
Q4QZ40
Q53H04
Q53H06
Q69EZ7
Q7Z7P3
Q9UCA1
Already parsed 9 XML elements.          


CALL EXAMPLE 2:
COMMAND LINE:     python3 callDealer.py P00734.xml sequence
OUTPUT:           
MAHVRGLQLPGCLALAALCSLVHSQHVFLAPQQARSLLQRVRRANTFLEEVRKGNLEREC
VEETCSYEEAFEALESSTATDVFWAKYTACETARTPRDKLAACLEGNCAEGLGTNYRGHV
NITRSGIECQLWRSRYPHKPEINSTTHPGADLQENFCRNPDSSTTGPWCYTTDPTVRRQE
CSIPVCGQDQVTVAMTPRSEGSSVNLSPPLEQCVPDRGQQYQGRLAVTTHGLPCLAWASA
QAKALSKHQDFNSAVQLVENFCRNPDGDEEGVWCYVAGKPGDFGYCDLNYCEEAVEEETG
DGLDEDSDRAIEGRTATSEYQTFFNPRTFGSGEADCGLRPLFEKKSLEDKTERELLESYI
DGRIVEGSDAEIGMSPWQVMLFRKSPQELLCGASLISDRWVLTAAHCLLYPPWDKNFTEN
DLLVRIGKHSRTRYERNIEKISMLEKIYIHPRYNWRENLDRDIALMKLKKPVAFSDYIHP
VCLPDRETAASLLQAGYKGRVTGWGNLKETWTANVGKGQPSVLQVVNLPIVERPVCKDST
RIRITDNMFCAGYKPDEGKRGDACEGDSGGPFVMKSPFNNRWYQMGIVSWGEGCDRDGKY
GFYTHVFRLKKWIQKVIDQFGE

Already parsed 1 XML elements.
'''
