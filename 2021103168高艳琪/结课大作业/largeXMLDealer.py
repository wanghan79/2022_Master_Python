#!/usr/bin/env python
# coding:utf-8
"""
  Author:  高艳琪
  Purpose: To parse the large XML files more than 500M
  Created: 17/6/2022
"""
from lxml import etree
from os import path
from optparse import OptionParser
def dealwithElement(elem):
    dict_elem = {}
    child_list = []
    # 函数isinstance()可以判断一个变量的类型
    if isinstance(elem, object):
        dict_elem['tag'] = elem
        dict_elem['value']=elem.text
        for child in elem:
            if isinstance(child, object):
                child_list.append(dealwithElement(child))
        if child_list == []:
            dict_elem['child'] = None
        else:
            dict_elem['child'] = child_list
    return dict_elem
class largeXMLDealer():
    def __init__(self, func):
        self._func = func
    def __call__(self, *args, **kwargs):
        print('largeXMLDealer')
        count = self.parse(*args, **kwargs)
        print("Already parsed %d XML elements." % count)
    def parse(self, *args, **kwargs):
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
        #lxml 的 iterparse 方法是 ElementTree API 的扩展。iterparse 为所选的元素上下文返回一个 Python 迭代器。
        #它接受两个有用的参数：要监视的事件元组和标记名。
        context = etree.iterparse(args[0], events=('start',), tag=tag)
        #对指定的标记和事件进行简单迭代
        for event, elem in context:
            # 调用外部函数来处理这里的元素
            chs = list(elem)
            try:
                print(dealwithElement(elem))
            except Exception:
                raise Exception("Something wrong in function parameter: func4Element")
            finally:
                #在每次循环结束后回收内存。这包括对已经处理的子节点和文本节点的引用，以及对当前节点前面的兄弟节点的引用。这些引用中来自根节点的引用也被隐式地保留
                elem.clear()
                count = count + 1
                while elem.getprevious() is not None:
                    del elem.getparent()[0]
        del context
        # 返回已解析的元素个数
        return count
    def _getNamespace(self, fileName):
        if not path.isfile(fileName) or not fileName.endswith("xml"):
            raise FileNotFoundError
        result = ''
        es = ('start-ns',)
        context = etree.iterparse(fileName, events=es)
        for event, elem in context:
            prefix, result = elem
            break
        del context
        return result
def main():
    # Construct the usage.
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file",  default='P00734.xml', action="store_true",
                      help="XML file name")
    parser.add_option("-p", "--print", dest="bPrint", default=False, action="store_true",
                      help="Print results on the screen.")
    parser.add_option("-o", "--output", type="string", dest="outputFile", default=None,
                      help="Output the results to a file.")
    parser.add_option("-t", "--tag", type="string", dest="tag", default="authorList",
                      help="The XML tag interested to parse.")
    (options, args) = parser.parse_args()
    filePath = path.normpath(options.file)
    if not path.isfile(filePath) or not filePath.endswith("xml"):
        raise Exception("The input file is not exist or a available XML file.")
    DealerStrat_1(filePath, options.tag)
@largeXMLDealer
def DealerStrat_1(*args, **kwargs):
    print("start")
if __name__ == "__main__":
    main()
