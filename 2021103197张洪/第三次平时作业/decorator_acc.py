from self_defined_struct_sampling import SelfDefinedStructSampling


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


sss = SelfDefinedStructSampling()
param = {"struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 100)}, }, "num": 20}
result = sss.sampling(**param)

struct = list()
for item in result:
    itemList = list()
    itemList.append(item)
    if item[0] >= item[1]:
        tmp = 1
    else:
        tmp = 0
    itemList.append(tmp)
    struct.append(itemList)


@ACC(struct=struct)
def pred1(struct):
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


print("acc is ", pred1(result))
