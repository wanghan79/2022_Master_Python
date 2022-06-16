import random

class matrixValue():
    def getValue(self, *args):
        intValue = args[0]['int']
        floatValue = args[0]['float']
        boolValue = args[0]['bool']
        num = args[0]['num']

        label = list()
        for _ in range(0, num):
            tmp = random.getrandbits(1)
            label.append(tmp)


        tp, fp, tn, fn = 0, 0, 0, 0
        for i in range(0, num):
            if boolValue[i] == 1:
                if label[i] == boolValue[i]:
                    tp = tp + 1
                else:
                    fn = fn + 1
            else:
                if label[i] == boolValue[i]:
                    tn = tn + 1
                else:
                    fp = fp + 1
        return tp, fp, tn, fn