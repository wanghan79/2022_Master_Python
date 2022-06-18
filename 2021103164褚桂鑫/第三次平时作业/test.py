from cal_acc_mcc import pred1, pred2
import string

if __name__ == '__main__':
    """
    #验证准确率 acc
    paras1 = {'num': 10, 'struct': {
        "int": {'datarange': (0, 100)},
        'float': {"datarange": (0, 1000)},
        "str": {'datarange': string.ascii_uppercase, 'strlen': 10},
        "bool": {'datarange': (0, 1)}
    }}
    pred1(**paras1)

    args2 = {'num': 30}
    paras2 = {'num': 30, 'struct': {
        "int": {'datarange': (0, 100)},
        'float': {"datarange": (0, 1000)},
        "str": {'datarange': string.ascii_uppercase, 'strlen': 10},
        "bool": {'datarange': (0, 1)}
    }}
    pred2(args2, **paras2)
    """



    # 验证马修斯相关系数（Matthews correlation coefficient）
    paras1 = {
        'row': {'num': 10, 'datarange': (0, 1)},
        'col': {'num': 5, 'datarange': (0, 1)}
    }
    pred1(**paras1)
    paras2 = {
        'row': {'num': 10, 'datarange': (0, 1)},
        'col': {'num': 30, 'datarange': (0, 1)}
    }
    args2 = {'num': 30}
    pred2(args2, **paras2)
