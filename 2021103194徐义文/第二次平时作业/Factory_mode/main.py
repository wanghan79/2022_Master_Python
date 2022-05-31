from dataFactoryInterface import dataFactoryInterface

if __name__ == '__main__':
    interface = dataFactoryInterface()

    obj = interface.create('int')
    paras = {'datarange': (0, 10), 'num': 5}
    result = obj.sampling(**paras)
    print(result)
