import pandas as pd

#读取数据集abalone
df=pd.read_table('./abalone.txt',header=None)
# print(df.head(100))
# print(df.shape)

#提取鲍鱼的数据，存到x_data里面

x_data=df[[0,1,2,3,4,5,6,7]]

#鲍鱼年龄，存到y_target里面
y_target=df[8]

# print(x_data)
# print(y_target)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x_data,y_target,test_size=0.33)
#回归算法
from sklearn.linear_model import LinearRegression
lrg=LinearRegression()
lrg.fit(X_train,y_train)
# print(lrg.intercept_)
y_pred=lrg.predict(X_test)

#对比输出真实数据和预测数据
#对比数据就能发现学习
# for (true_age,pred_age) in zip (y_test.values.reshape((-1)),y_pred):
#     print('真实：'+str(true_age)+'预测：'+str(pred_age))

from sklearn.svm import SVR
svr=SVR()
svr.fit(X_train,y_train)
svr.predict(X_test)
print(svr)
for (true_age,pred_age) in zip (y_test.values.reshape((-1)),y_pred):
    print('真实：'+str(true_age)+'预测：'+str(pred_age))