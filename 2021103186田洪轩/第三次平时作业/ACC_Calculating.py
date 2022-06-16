from matrixValue import *
class ACC():
    def __init__(self, func):
        self.funcs = func
        self.matrix = matrixValue()

    def __call__(self, *args, **kwargs):
        tp, fp, tn, fn = self.matrix.getValue(*args)
        acc = float((tp + tn) / (tp + tn + fp + fn))
        self.funcs(*args, **kwargs)
        return acc