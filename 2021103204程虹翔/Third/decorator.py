from dataFactoryInterface import DataFactoryInterface
import math


def getMatrix(*args):
    int_list = args[0].get('Int')
    float_list = args[0].get('Float')
    bool_list = args[0].get('Bool')
    num = args[0].get('num')
    tp, fp, tn, fn = 0, 0, 0, 0
    for i in range(0, num):
        if bool_list[i] == 1:
            if int_list[i] <= float_list[i]:
                tp = tp + 1
            else:
                fp = fp + 1
        else:
            if int_list[i] <= float_list[i]:
                tn = tn + 1
            else:
                fn = fn + 1
    return tp, fp, tn, fn


def accCalculator(func):
    def wrapper(*args, **kwargs):
        tp, fp, tn, fn = getMatrix(*args)
        acc = float((tp + tn) / (tp + tn + fp + fn))
        print("ACC : " + str(acc))
    return wrapper


def mccCalculator(func):
    def wrapper(*args, **kwargs):
        tp, fp, tn, fn = getMatrix(*args)
        mcc = float(tp * tn - fp * fn) / (math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)))
        print("MCC : " + str(mcc))
    return wrapper


@accCalculator
def predAcc(*args, **kwargs):
    pass


@mccCalculator
def predMcc(*args, **kwargs):
    pass


if __name__ == '__main__':
    name_list = ['Int', 'Float', 'Bool']
    value_dic = {}
    interface = DataFactoryInterface()
    paragrams = {'datarange': (0, 10), 'num': 10}
    value_dic['num'] = paragrams.get('num')

    for name in name_list:
        obj = interface.create(name)
        result = obj.sampling(**paragrams)
        value_dic[name] = result
    predAcc(value_dic)
    predMcc(value_dic)