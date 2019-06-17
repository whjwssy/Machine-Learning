import math
import operator

#读取文件，获取147个训练数据集
def getTrainingSet(filename,trainingSet=[]):
    fp = open(filename)
    dataset = []
    for linea in fp.readlines():
        #数据预处理
        line = linea.replace('\n', '').replace('\t', ',')
        linetest = line.split(',')
        dataset.append(linetest)
    fp.close()
    print(dataset)
    print('len(dataset):' + str(len(dataset)))

    for x in range(len(dataset)):
        for y in range(4):
            dataset[x][y] = float(dataset[x][y])#将数据转换成float型
        trainingSet.append(dataset[x])



# 计算参数的欧式距离
def euclideanDistance(instance1, instance2, lenth):
    distance = 0
    for x in range(lenth):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# 传递每一个测试实例，并将它同训练集每一个实例求取欧式距离，并且排序，获取k个近邻
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    lenth = len(testInstance)
    for x in range(len(trainingSet)):  #计算测试的数据与每个训练数据的距离
        dist = euclideanDistance(testInstance, trainingSet[x], lenth)
        #把距离写入训练实例以供排序
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


# 根据k近邻少数服从多数的原则，将测试数据分类
def getResponse(neighbors):
    Votes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in Votes:
           Votes[response] += 1
        else:
            Votes[response] = 1
    sort = sorted(Votes.items(), key=operator.itemgetter(1), reverse=True)
    return sort[0][0]


def main():
    trainingSet = []
    testSet = [[5.4,3.4,1.5,0.4],[6.1,2.9,4.7,1.4],[7.9,3.8,6.4,2]]#测试数据三组
    getTrainingSet(r'/Users/wanghongjin/Desktop/flower.txt', trainingSet)
    print('train set:' + repr(len(trainingSet)))
    print('test set:' + repr(len(testSet)))
    print(testSet)
    predictions = []
    k = 6 #根据题设要求k值取6
    for x in range(len(testSet)):  # 循环并测试所有测试集，输出测试结果与真实标签。
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('测试集'+repr(testSet[x])+'的分类为'+repr(result))

if __name__ == '__main__':
    main()