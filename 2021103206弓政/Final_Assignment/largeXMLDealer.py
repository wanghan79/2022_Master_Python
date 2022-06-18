#!/usr/bin/env python
# coding:utf-8
"""
  Author:  H.Wang --<>
  Purpose: To parse the large XML files more than 500M
  Created: 4/4/2016
"""

from lxml import etree
from os import path
from optparse import OptionParser


class largeXMLDealer():
    """
    读大型xml的所有功能都集成在里面，并且提供调用的接口
    """

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        # 这里parse的参数为*args和**kwargs是为了顺利实现装饰器
        count = self.parse(*args, **kwargs)
        print("Already parsed %d XML elements." % count)

    # 原来的：def parse(self, fileName, elemTag, func4Element=None):
    # elemTag改成更加合理*args
    # func4Element传进来操作方法
    def parse(self, fileName, func4Element=None, *args):
        """"""
        if not path.isfile(fileName) or not fileName.endswith("xml"):
            raise FileNotFoundError

        count = 0
        es = ('end',)
        ns = self._getNamespace(fileName)
        ns = "{%s}" % ns

        # 使用*args参数传进来需要解析的标签的列表,此处先处理一下args参数
        # 如果有标签列表,则使用用户输入的标签列表，若用户没有输入，则解析整个xml文件
        if args[0]:
            tag_list = args[0]
        else:
            tag_list = ['entry']

        # 通过循环可以解析多个需要的标签
        for element_tag in iter(tag_list):
            tag = ns + element_tag
            context = etree.iterparse(fileName, events=('start',), tag=tag)

            for event, elem in context:
                # Call the outside function to deal with the element here
                chs = list(elem)
                try:
                    # 通过断言,如果没有传func4Element参数,则给出提示
                    assert func4Element, 'func4Element is None, you should use parameter'
                    dict_elem = func4Element(elem)
                    print(dict_elem)
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


def main():
    """

    """
    # Construct the usage.
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-p", "--print", dest="bPrint", default=False, action="store_true",
                      help="Print results on the screen.")
    parser.add_option("-o", "--output", type="string", dest="outputFile", default=None,
                      help="Output the results to a file.")
    parser.add_option("-t", "--tag", type="string", dest="tag", default="",
                      help="The XML tag interested to parse.")

    # Parse the options and args input by users.
    (options, args) = parser.parse_args()

    # Check the correction of users input and call the functions of class DoSomething.
    if (len(args) != 1):
        parser.error("You have not input the XML file name")

    filePath = path.normpath(args[0])
    if not path.isfile(filePath) or not filePath.endswith("xml"):
        raise Exception("The input file is not exist or a available XML file.")
    # Call XML parser
    largXML = largeXMLDealer()
    count = largXML.parse(filePath, options.tag)
    print("Parsed %10d XML elements." % count)


if __name__ == "__main__":
    main()
