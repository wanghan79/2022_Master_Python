from lxml import etree
from os import path
from optparse import OptionParser


class Read_XML():
    """
    """

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        count = self.parse(*args, **kwargs)
        print("Already parsed %d XML elements." % count)


    def parse(self, *args, **kwargs):
        """"""
        if not path.isfile(args[0]) or not args[0].endswith("xml"):
            raise FileNotFoundError

        count = 0
        es = ('end',)
        ns = self._getNamespace(args[0])
        ns = "{%s}" % ns
        if args[1] != '':
            tag = ns + args[1]
        else:
            tag = ns + 'uniprot'
        context = etree.iterparse(args[0], events=('start',), tag=tag)

        for event, elem in context:
            # Call the outside function to deal with the element here
            chs = list(elem)
            try:
                if args[2] == None:
                    print('none')
                else:
                    print(args[2](elem))
            except Exception:
                raise Exception("Something wrong in function parameter: func4Element")
            finally:
                elem.clear()
                count = count + 1
                while elem.getprevious() is not None:
                    del elem.getparent()[0]
        del context
        # Return how many elements had been parsed
        return count

    def _getNamespace(self, fileName):
        """"""
        if not path.isfile(fileName) or not fileName.endswith("xml"):
            raise FileNotFoundError
        result = ''
        es = ('start-ns',)
        context = etree.iterparse(fileName, events=es)
        for event, elem in context:
            prefix, result = elem
            # print("%s, %d"%(elem, len(elem)))
            break
        del context
        return result

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

@Read_XML
def DealerStrat(*args, **kwargs):
    print('start')


if __name__ == "__main__":
    fileName = './test.xml'
    elemTag = 'component'
    DealerStrat(fileName, elemTag, dealwithElement)