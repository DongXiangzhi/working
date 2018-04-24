from sklearn import datasets
from sklearn.datasets.samples_generator import make_classification
from sklearn import preprocessing
from sklearn.preprocessing import Normalizer



iris=datasets.load_iris() #导入数据集
X=iris.data
y=iris.target #获得样本label
z=iris.keys()
print(z)
print(iris.feature_names)
print(iris.DESCR)
print(iris.target_names)
print(y)
print(X)

Normalizer().fit_transform(iris.data)



# print(X,y)
#
# X,y=make_classification(n_samples=6,
#                        n_features=5,
#                        n_informative=2,
#                       n_redundant=2,
#                       n_classes=2,
#                       n_clusters_per_class=2,
#                       scale=1.0,
#                       random_state=20)
# # for x_,y_ in zip(X,y):
# #     print(y_,end=": ")
# #     print(x_)
#
#
# data = [[0, 0], [0, 0], [1, 1], [1, 1]]
# # 1. 基于mean和std的标准化
# scaler = preprocessing.StandardScaler().fit(train_data)
# scaler.transform(train_data)
# scaler.transform(test_data)

# 2. 将每个特征值归一化到一个固定范围
# scaler = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit(train_data)
# scaler.transform(train_data)
# scaler.transform(test_data)
#feature_range: 定义归一化范围，注用（）括起来
