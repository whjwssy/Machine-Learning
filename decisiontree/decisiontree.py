from math import log

#根据题干中所给题目创建数据集
def createDataSet():
    #将数据集特征转化为0，1，2
    #其中Age：Youth 0、Middle_aged 1；Income：High 0、Medium 1、Low 2；
    #Student：No 0、Yes 1；Credit_rating： Fair 0、Excellent 1
    dataSet = [[0, 0, 0, 0, 'no'],
               [0, 0, 0, 1, 'no'],
               [1, 0, 0, 0, 'yes'],
               [2, 1, 0, 0, 'yes'],
               [2, 2, 1, 0, 'yes'],
               [2, 2, 1, 1, 'no'],
               [1, 2, 1, 1, 'yes'],
               [0, 1, 0, 0, 'no'],
               [0, 2, 1, 0, 'yes'],
               [2, 1, 1, 0, 'yes'],
               [0, 1, 1, 1, 'yes'],
               [1, 1, 0, 1, 'yes'],
               [1, 0, 1, 0, 'yes'],
               [2, 1, 0, 1, 'no']]
    #分类属性
    labels = ['age', 'income', 'student', 'credit_rating']
    #返回数据集和分类属性
    return dataSet, labels


#计算经验熵
def getHD(dataSet):
    lenDataSet=len(dataSet)
    p={}
    h=0.0
    for data in dataSet:
        #获取类别标签
        currentLabel=data[-1]
        if currentLabel not in p.keys():
            p[currentLabel]=0
        #增加类别标签值
        p[currentLabel]+=1
    for key in p:
        px=float(p[key])/float(lenDataSet)  #计算某个标签的概率
        h-=px*log(px,2)  #计算经验熵
    return h

#根据特征将数据集分类dataSet为要划分的数据集,feature为给定的特征，value为给定特征的具体值
def getsubData(dataSet,feature,value):
    subDataSet=[]
    for data in dataSet:
        subData=[]
        if data[feature]==value:
            subData=data[:feature]
            subData.extend(data[feature+1:])
            subDataSet.append(subData)
    return subDataSet

#选取信息增益最大的特征
def chooseFeature(dataSet):
    lenFeature=len(dataSet[0])-1
    shanInit=getHD(dataSet)
    feature=[]
    inValue=0.0
    bestFeature=0
    for i in range(lenFeature):
        shanCarry=0.0
        feature=[example[i] for example in dataSet]
        feature=set(feature)
        for feat in feature:
            subData=getsubData(dataSet,i,feat)
            prob=float(len(subData))/float(len(dataSet))
            shanCarry+=prob*getHD(subData)
        outValue=shanInit-shanCarry
        if (outValue>inValue):
            inValue=outValue
            bestFeature=i
    return bestFeature


#构建决策树
def createTree(dataSet,label):
    classList=[example[-1] for example in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]
    featBest=chooseFeature(dataSet)
    feature=[example[featBest] for example in dataSet]
    featValue=set(feature)
    newLabel=label[featBest]
    del(label[featBest])
    Tree={newLabel:{}}
    for value in featValue:
        subLabel=label[:]
        Tree[newLabel][value]=createTree(getsubData(dataSet,featBest,value),subLabel)
    return Tree

if __name__ == '__main__':
    #创建数据集
    dataSet, label = createDataSet()
    #打印生成的决策树
    print("决策树：" + str(createTree(dataSet, label)))
