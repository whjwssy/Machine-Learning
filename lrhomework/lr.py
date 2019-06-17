from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors

def loadData():
    f = open('/Users/wanghongjin/Desktop/flower.txt')
    dataset  = []
    train_x = []
    train_y = []
    test_x = []
    test_y = []
    i = 0
    j = 0
    categoryMap = {}
    for lines in f.readlines():
        line = lines.replace('\n', '').replace('\t', ';')
        linesp = line.split(';')
        dataset.append(linesp)
        if not linesp[len(linesp) - 1] in categoryMap.keys():
            categoryMap[linesp[len(linesp) - 1]] = i
            i += 1
        dataset[j][4] = i-1
        j += 1
        f.close()
    random.shuffle(dataset)
    for x in range(0, int(len(dataset)*0.8)):
        for y in range(4):
            dataset[x][y] = float(dataset[x][y])
        train_x.append(dataset[x][:4])
        train_y.append(dataset[x][4])
    for i in range(int(len(dataset)*0.8),len(dataset)):
        for j in range(4):
            dataset[i][j] = float(dataset[i][j])
        test_x.append(dataset[i][:4])
        test_y.append(dataset[i][4])
    # print(train_x)
    # print(mat(dataset))
    return mat(train_x), train_y, mat(test_x), test_y,categoryMap,mat(dataset)



def softmax(X):
    return np.exp(X) / np.sum(np.exp(X))


def train(digits, labels, maxIter=100, alpha=0.1):
    weights = np.random.uniform(0, 1, (3, 4))
    for iter in range(maxIter):
        for i in range(len(digits)):
            x = digits[i].reshape(-1, 1)
            y = np.zeros((3, 1))
            y[int(labels[i])] = 1
            y_ = softmax(np.dot(weights, x))
            weights -= alpha * (np.dot((y_ - y), x.T))
    return weights


def predict( digit,weights):
    return np.argmax(np.dot(weights, digit.T))

if __name__ == '__main__':
    trainDigits, trainLabels,testDigits,testLabels,categotryMap,dataset = loadData()
    weights=train(trainDigits, trainLabels, maxIter=500)
    accuracy = 0
    N = len(testDigits)
    for i in range(N):
        digit = testDigits[i]
        label = testLabels[i]
        predict1 = predict(digit,weights)
        if (predict1 == label):
            accuracy += 1
        print(">>>predict:%d, actual:%d" % (predict1, label))
    print("**************accuracy:%.1f%%" % (accuracy / N * 100)+" *****************")



