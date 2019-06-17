import math

def loadDataset(filename,dataSet =[],num=0):
    fp = open(filename)
    dataset = []
    for linea in fp.readlines():
        # 数据预处理
        line = linea.replace('\n', '').replace('\t', ',')
        linetest = line.split(',')
        dataset.append(linetest)
    fp.close()
    num = len(dataset)
    for x in range(len(dataset)):
            dataset[x][0] = int(dataset[x][0])  # 将数据转换成float型
            dataset[x][2] = int(dataset[x][2])
            dataSet.append(dataset[x])

def getResult(testSet,dataSet):
    p1num = 0
    m = 0
    n = 0
    a = 0
    b = 0
    for x in range(len(dataSet)):
        if dataSet[x][2] == 1:
            p1num +=1
    pLabel1 = p1num/float(len(dataSet))
    #按类别，此时为类别为1
    for x in range(len(dataSet)):
        if dataSet[x][0] == testSet[0] and dataSet[x][2] == 1:
            n +=1
    p1testx1 = (n/float(len(dataSet)))/pLabel1
    for x in range(len(dataSet)):
        if dataSet[x][1] == testSet[1] and dataSet[x][2] == 1:
            m +=1
    p1testx2 = (m/float(len(dataSet))) * (1/pLabel1)
    p1 =pLabel1 * p1testx1 * p1testx2
    # 按类别，此时为类别为-1
    for x in range(len(dataSet)):
        if dataSet[x][0] == testSet[0] and dataSet[x][2] == -1:
            a += 1
    p2testx1 = (a / float(len(dataSet))) / (1-pLabel1)
    for x in range(len(dataSet)):
        if dataSet[x][1] == testSet[1] and dataSet[x][2] == -1:
            b += 1
    p2testx2 = (b / float(len(dataSet))) * (1 / (1-pLabel1))
    p2 = (1-pLabel1) * p2testx1 * p2testx2
    print(testSet)
    if p1 > p2:
        print('p1>p2,且分别为'+str(p1)+'和'+str(p2))
        return "分类结果为：Y = 1"
    else:
        print('p2>p1,且分别为' + str(p2)+'和'+str(p1))
        return "分类结果为：Y = -1"


def main():
    dataSet = []
    loadDataset('/Users/wanghongjin/Desktop/dataset.txt',dataSet)
    testSet = [2,'s']
    print(dataSet)
    print('len(dataset):' + str(len(dataSet)))
    p = getResult(testSet,dataSet)
    print(str(p))
if __name__ == '__main__':
    main()