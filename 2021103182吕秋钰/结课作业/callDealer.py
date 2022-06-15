from largeXMLDealer import largeXMLDealer


def dealwithElement(elem):
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
def DealerStrat(*args, **kwargs):
    print('start')


if __name__ == "__main__":
    xml_file_name = './P00734.xml'
    elemTag = 'protein'
    DealerStrat(xml_file_name, elemTag, dealwithElement)