import pandas as pd
import numpy as np

#从网络上获取原始数据
#创建特征列表

columnNames=['Sample code number: id number',
'Clump Thickness',
'Uniformity of Cell Size',
'Uniformity of Cell Shape',
'Marginal Adhesion',
'Single Epithelial Cell Size',
'Bare Nuclei',
'Bland Chromatin',
'Normal Nucleoli',
'Mitoses',
'Class']
data=pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',names=columnNames)
# print(data)

data=data.replace(to_replace='?',value=np.NaN)
data=data.dropna(how='any')
print(data.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(data[columnNames[0:9]],data[columnNames[10]],test_size=0.25 ,random_state=30)
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
X_train=ss.fit_transform(X_train)
X_test=ss.fit_transform(X_test)

#逻辑回归LR
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier

lr=LogisticRegression()
#随机参数梯度估计
sgdc=SGDClassifier()
lr.fit(X_train,y_train)

lr_y_predict=lr.predict(X_test)
#调用SGDClassifier中的fit来训练模型参数
sgdc.fit(X_train,y_train)
sgdc_y_predict=sgdc.predict(X_test)

print(lr_y_predict)
print(sgdc_y_predict)

from sklearn.metrics import classification_report
print('LR的准确率：'+str(lr.score(X_test,y_test)))

print(classification_report(y_test,lr_y_predict,target_names=['Benign','Malignant']))
print(classification_report(y_test,sgdc_y_predict,target_names=['Benign','Malignant']))
