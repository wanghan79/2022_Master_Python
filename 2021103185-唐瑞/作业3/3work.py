import random

def selfDefinedStructSampling(*args, **kwargs):
    result = list()
    try:
        assert ('num' in kwargs.keys() or 'struct' in kwargs.keys())
        for index in range(0, kwargs.get('num')):
            element = list()
            for key, value in kwargs.get("struct").items():
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == "float":
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == "lable":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                else:
                    break
                element.append(tmp)
            result.append(element)
    except BaseException as EOR:
        print(EOR)
    return result
def Value(result):
    TP, TN, FP, FN = 0, 0, 0, 0
    for item in result:
        x1 = item[0]
        x2 = item[1]
        if x1 > (-1 * x2):
            Y = 1
        else:
            Y = 0
        if item[2] == 0 and Y == 0:
            TN += 1
        elif item[2] == 0 and Y == 1:
            FP += 1
        elif item[2] == 1 and Y == 1:
            TP += 1
        else:
            FN += 1
    return TP, TN, FP, FN
def ACC(origin):
    def wrapper(*args, **kwargs):
        res = origin(*args, **kwargs)
        TP, TN, FP, FN = Value(res)
        try:
            print("ACC = ", ((TP + TN) / (TP + FP + FN + TN)))
        except BaseException as e:
            print(e)
        return res

    return wrapper


def MCC(origin):
    def wrapper(*args, **kwargs):
        res = origin(*args, **kwargs)
        TP, TN, FP, FN = Value(res)
        try:
            N = TN + TP + FN + FP
            S = (TP + FN) / N
            P = (TP + FP) / N
            print("MCC:", ((TP / N) - (S * P) / (P * S * (1 - S) * (1 - P)) ** 0.5))
        except BaseException as EOR:
            print(EOR)
        return res

    return wrapper



@ACC
def pred1(struct):
    result = selfDefinedStructSampling(**struct)
    return result


@MCC
def pred2(*args, **kwargs):
    result = selfDefinedStructSampling(*args, **kwargs)
    return result


if __name__ == "__main__":
    struct = {"num": 100, "struct": {"int": {"datarange": (-200, 200)}, "float": {"datarange": (-200, 200)},
                                     "lable": {"datarange": (0, 1)}}}
    pred1(struct)
    pred2(**struct)