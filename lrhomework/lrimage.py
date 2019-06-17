# !/usr/bin/env python
# encoding: utf-8
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn import model_selection
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def iris_type(s):
    class_label={b'Iris-setosa':0,b'Iris-versicolor':1,b'Iris-virginica':2}
    return class_label[s]

filepath='/Users/wanghongjin/Desktop/a.txt' #文件路径
data=np.loadtxt(filepath,dtype=float,delimiter=',',converters={4:iris_type})
X ,y=np.split(data,(4,),axis=1)
x=X[:,0:2]#取前两列
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,random_state=1,test_size=0.2)
classifier=Pipeline([('sc',StandardScaler()),('clf',LogisticRegression())])
classifier.fit(x_train,y_train.ravel())

def show_accuracy(y_hat,y_test,parameter):
    pass

y_hat=classifier.predict(x_train)
y_hat=classifier.predict(x_test)



#print(y_hat[2])
setosa_ = []
versicolor_= []
virginica_ = []
for i in range(len(x_test)):
    if y_hat[i] == 0:
        setosa_.append(x_test[i])
    if y_hat[i] == 1:
        versicolor_.append(x_test[i])
    if y_hat[i] == 2:
        virginica_.append(x_test[i])

setosa = np.array(setosa_)
versicolor = np.array(versicolor_)
virginica = np.array(virginica_)
#print(versicolor_)

x1_min, x1_max = x[:, 0].min(), x[:, 0].max()
x2_min, x2_max = x[:, 1].min(), x[:, 1].max()
x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]
test = np.stack((x1.flat, x2.flat), axis=1)
hat = classifier.predict(test)
hat = hat.reshape(x1.shape)
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
cm_light = mpl.colors.ListedColormap(['#a0a0a0', '#a0d0ff', '#A0A0FF'])
cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
alpha=0.5
plt.pcolormesh(x1, x2, hat, cmap=cm_light)
#plt.plot(x[:, 0], x[:, 1], 'o', alpha=alpha, color='blue', markeredgecolor='k')
# plt.scatter(x_test[:, 0], x_test[:, 1], s=120, facecolors='none', zorder=10)
plt.scatter(setosa[:,0],setosa[:,1] ,color='red', marker='o', label='setosa')
plt.scatter(versicolor[:,0],versicolor[:,1],color='blue', marker='x', label='versicolor')
plt.scatter(virginica[:,0],virginica[:,1], color ='green', marker='s', label='Virginica')

plt.xlabel(u'Sepal.Length', fontsize=13)
plt.ylabel(u'Sepal.Width', fontsize=13)
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.title(u'LogisticRegression ', fontsize=15)
plt.grid()
plt.show()