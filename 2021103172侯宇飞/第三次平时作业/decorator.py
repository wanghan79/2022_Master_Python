import math
from getMatrix import GetMatrix

class Decorator():
    def __init__(self, func):
        self._func = func
        self.matrix = GetMatrix()

    def __call__(self, *args, **kwargs):
        tp, fp, tn, fn = self.matrix.get_all(*args)
        mcc = float(tp * tn - fp * fn) / (
            math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))) + float(0.000001)
        acc = float((tp + tn) / (tp + tn + fp + fn))
        self._func(*args, **kwargs)
        # print('mcc:'+str(mcc)+' acc:'+str(acc))
        return str(mcc), str(acc)


