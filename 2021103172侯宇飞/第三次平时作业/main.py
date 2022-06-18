from decorator import Decorator
from dataFactoryInterface import dataFactoryInterface

@Decorator
def pred(*args, **kwargs):
    #print(args, **kwargs)
    pass

if __name__ == '__main__':
    name_list = ['int', 'float', 'bool']
    value_dic = {}
    interface = dataFactoryInterface()
    paras = {'datarange': (0, 10), 'num': 10}
    value_dic['num'] = paras.get('num')

    for name in name_list:
        obj = interface.create(name)
        result = obj.sampling(**paras)
        value_dic[name] = result
    mcc, acc = pred(value_dic)
    print('pred:')
    print('acc:' + acc)
    print('mcc:' + mcc)