import random
from sklearn.metrics import matthews_corrcoef
class ACC:
    def __init__(self, struct):
        self.struct = struct

    def __call__(self, pred):
        def wrapper(*args, **kwargs):
            struct_pred = pred(*args, **kwargs)
            label_list = list()
            label_pred_list = list()
            for _, label, _ in struct_pred:
                label_pred_list.append(label)
            for _, label in self.struct:
                label_list.append(label)
            ret = list(set(label_pred_list) ^ set(label_list))
            return (1 - (len(ret) / len(self.struct)))

        return wrapper

class MCC:
    def __init__(self, struct):
        self.struct = struct

    def __call__(self, pred):
        def wrapper(*args, **kwargs):
            struct_pred = pred(*args, **kwargs)
            label_list = list()
            label_pred_list = list()
            for _, label, _ in struct_pred:
                label_pred_list.append(label)
            for _, label in self.struct:
                label_list.append(label)
            return matthews_corrcoef(label_list, label_pred_list)

        return wrapper

class SelfDefinedStructSampling():

    def __init__(self):
        self.__name = "SelfDefinedStructSampling"

    def sampling(self, **kwargs):
        result = list()
        for index in range(0, kwargs.get('num')):
            element = list()
            for key, value in kwargs.get("struct").items():
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == "float":
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result

s = SelfDefinedStructSampling()
param = {"struct": {"int": {"datarange": (0, 200)}, "float": {"datarange": (0, 200)}, }, "num": 10}
result = s.sampling(**param)

struct = list()
for item in result:
    itemList = list()
    itemList.append(item)
    if (item[0] >= item[1]):
        tmp = 1
    else:
        tmp = 0
    itemList.append(tmp)
    struct.append(itemList)

@ACC(struct)
def pred1(struct):
    struct_pred = list()
    for item in struct:
        itemList = list()
        itemList.append(item)
        if item[0] >= item[1]:
            tmp = 1
        else:
            tmp = 0
        itemList.append(itemList.append(tmp))
        struct_pred.append(itemList)
    return struct_pred

@MCC(struct)
def pred2(*args, **kwargs):
    struct = list(args)
    struct = struct[0]
    struct_pred = list()
    for item in struct:
        itemList = list()
        itemList.append(item)
        if item[0] >= (item[1] + 100):
            tmp = 1
        else:
            tmp = 0
        itemList.append(itemList.append(tmp))
        struct_pred.append(itemList)
    return struct_pred

print("ACC= ", pred1(result))
print("MCC= ", pred2(result))
