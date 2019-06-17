import os

#训练集按照题目给定写入数组，y值对应1与-1
training_set = [[(3, 3), 1], [(4, 3), 1], [(1, 2), -1]]

#权重和偏置假设均为0，学习速率𝜂 为1
w = [0, 0]
b = 0
𝜂 = 1

#当实例被误分类时，按照梯度下降的方法更新w和b的值
def update(item):
    global w, b ,𝜂
    w[0] = w[0] + 𝜂  * item[1] * item[0][0]
    w[1] = w[1] + 𝜂  * item[1] * item[0][1]
    b = b + 𝜂  * item[1]
    #打印出每一次迭代的w值以及b值
    print(w,b)


# 计算yi(wxi+bi)的值以供判断是否大于0
def condition(item):
    global w, b
    res = 0
    for i in range(len(item[0])):
        res += item[0][i] * w[i]
    res += b
    res *= item[1]
    return res


# 检验是否被误分类
def check():
    flag = False
    for item in training_set:
        if condition(item) <= 0:
            flag = True
            update(item)
    if not flag:
        print("权重及偏置的最终结果为: w: " + str(w) + " b: " + str(b))
        os._exit(0)
    flag = False


if __name__ == "__main__":
    print("打印出每一次迭代的w与b值以供同纸质版对比")
    for i in range(1000):
        check()
    print("训练集不是线性可分 ")