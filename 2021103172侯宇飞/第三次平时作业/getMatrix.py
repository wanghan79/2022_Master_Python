class GetMatrix():
    def __init__(self):
        self.__name = 'GetMatrix'

    def get_all(self, *args):
        int_list = args[0].get('int')
        float_list = args[0].get('float')
        bool_list = args[0].get('bool')
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
