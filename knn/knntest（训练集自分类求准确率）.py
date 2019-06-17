# 导入库
import random  # 返回随机生成的一个实数，它在[0,1)范围内。
import math
import operator
import string


def loadDataset(filename, split, trainingSet=[], testSet=[]):
    fp = open(filename)
    dataset = []
    for linea in fp.readlines():
        line = linea.replace('\n', '').replace('\t', ',')
        linetest = line.split(',')
        dataset.append(linetest)

    fp.close()
    print(dataset)
    print('len(dataset):' + str(len(dataset)))
    for x in range(len(dataset)):  # 总共dataset的长度
        for y in range(4):
            dataset[x][y] = float(dataset[x][y])
        if random.random() < split:
            trainingSet.append(dataset[x])
        else:
            testSet.append(dataset[x])


# 计算一组参数的距离。

def euclideanDistance(instance1, instance2, lenth):
    distance = 0
    for x in range(lenth):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)



def getNeighbors(trainingSet, testInstance, k):
    distances = []
    lenth = len(testInstance) - 1  # 测试数据的维度
    for x in range(len(trainingSet)):  # 计算测试的数据与每个训练数据的距离
        dist = euclideanDistance(testInstance, trainingSet[x], lenth)
        distances.append((trainingSet[x], dist))  # 把每个距离都追加到distances当中###要多加一个括号做成一组传入参数
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors




def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][4]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    #print(str(classVotes))
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]



def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100


# 主函数定义
def main():
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset(r'/Users/wanghongjin/Desktop/flower.txt', split, trainingSet, testSet)
    print('train set:' + repr(len(trainingSet)))
    print('test set:' + repr(len(testSet)))

    predictions = []
    k = 6
    for x in range(len(testSet)):  # 循环并测试所有测试集，输出测试结果与真实标签。
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('>predicted=' + repr(result), 'actual=' + repr(testSet[x][-1]))

    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy:' + repr(accuracy) + '%')


if __name__ == '__main__':
    main()
