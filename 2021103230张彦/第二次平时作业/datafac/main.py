from datafac.dataFactoryInterface import dataFactoryInterface

if __name__ == '__main__':
    interface = dataFactoryInterface()

    obj = interface.create('int')
    paras = {'datarange': (0, 10), 'num': 3}
    result = obj.sampling(**paras)
    for item in result:
        print(item)
