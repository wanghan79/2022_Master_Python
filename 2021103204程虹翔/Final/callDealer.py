from largeXMLDealer import LargeXMLDealer
import sys


def dealwithElement(elem):
    """"""
    dict_elem = {}
    child_list = []
    if isinstance(elem, object):
        dict_elem[elem.tag] = elem.text
        for child in elem:
            if isinstance(child, object):
                child_list.append(dealwithElement(child))
        if not child_list:
            dict_elem['child'] = None
        else:
            dict_elem['child'] = child_list
    return dict_elem


@LargeXMLDealer
def DealerStart(*args, **kwargs):
    pass


if __name__ == "__main__":
    # #elemTag = list()
    # fileName = sys.argv[1]
    # for i in range(len(sys.argv) - 2):
    #     elemTag.append(sys.argv[i + 2])
    # DealStart(fileName, dealwithElement, elemTag)
    fileName = './P00734.xml'
    elemTag = ['accession', 'lineage']
    DealerStart(fileName, elemTag, dealwithElement)