from matrixValue import *
import math
class MCC():
    def __init__(self, func):
        self.funcs = func
        self.matrix = matrixValue()

    def __call__(self, *args, **kwargs):
        tp, fp, tn, fn = self.matrix.getValue(*args)
        mcc = float(tp * tn - fp * fn) / (math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))) + float(0.000001)
        self.funcs(*args, **kwargs)
        return mcc


