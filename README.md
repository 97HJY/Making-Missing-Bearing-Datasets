# Making-Missing-Bearing-Datasets
1）100、108~等十个数据文件是从官方的数据集摘出来的

2）之后用matlab（classes10code.m）处理为层c10signals.mat文件

3) 再用python（datasetSample.py）将其处理为十分类数据c10classes.mat和c10classes.mat。文件中包含打乱顺序的训练集（960×2048）、测试集（240×2048）。训练集（960×2048）： 960个样本，每个样本包含2048个数据点。

4）每360个样本数据中包含轴承内圈、滚动体和外圈三种故障数据各120个，每360个故障数据为一组中选15个故障数据假定为缺失。
