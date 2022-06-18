import random
struct={"num":10000,"struct":{"int":{"datarange":(0,100)},"float":{"datarange":(0,10000)},"bool":{"datarange":(0,1)}}}

#标签生成
def label_generator(num):
    list=[]
    for i in range(0,num):
        list.append(random.randint(0, 1))
    return list
label=label_generator(10000)
#生成预测
def pred1(num):
    result = list()
    for index in range(0, num):
        tmp = []
        tmp.append(random.randint(0, 100))
        tmp.append(random.uniform(0, 10000))
        tmp.append(random.randint(0, 1))
        result.append(tmp)
    return result
def pred2( **kwargs):
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
            elif key == "bool":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

#装饰器
def ACC(pred):
    def Accuracy(label,*args,**kwargs):
        prediction=pred(*args,**kwargs)

        n = 0
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        for i in label:
            if (i == 1 and prediction[n][2] == 1):
                TP += 1
            if (i == 0 and prediction[n][2] == 0):
                TN += 1
            if (i == 1 and prediction[n][2] == 0):
                FN += 1
            if (i == 0 and prediction[n][2] == 1):
                FP += 1
            n += 1
        return (TP+TN)/(TP+TN+FP+FN)
    return Accuracy
def MCC(pred):
    def Accuracy(label,*args,**kwargs):
        prediction=pred(*args,**kwargs)
        n=0
        TP=0
        TN=0
        FP=0
        FN=0
        for i in label:
            if (i==1 and prediction[n][2]==1) :
                TP+=1
            if (i==0 and prediction[n][2]==0) :
                TN+=1
            if (i==1 and prediction[n][2]==0) :
                FN+=1
            if (i==0 and prediction[n][2]==1) :
                FP+=1
            n+=1
        return (TP*TN-FP*FN)/(((TP+FP)*(FN+TP)*(FN+TN)*(FP+TN))**0.5)
    return Accuracy

#示例
@MCC
def pred2( **kwargs):
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
            elif key == "bool":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result
print(pred2(label,**struct))

