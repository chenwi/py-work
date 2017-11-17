#-*- coding:utf-8 -*-
# %matplotlib inline
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

data = sns.load_dataset("iris")
data.head()
# 萼片长度，萼片宽度，花瓣长度，花瓣宽度，种类
data['sepal_size']=data['sepal_length']*data['sepal_width']
data['petal_size']=data['petal_length']*data['petal_width']


sns.lmplot(x='sepal_size',y='petal_size',data=data)

# plt.plot(data['sepal_length'],data['sepal_width'])
g = sns.PairGrid(data,
                 x_vars=["species"],
                 y_vars=["sepal_size", "petal_size"],
                 aspect=2, size=4)
g.map(sns.violinplot, palette="pastel");


plt.show()
sns.jointplot(x='sepal_length',y='petal_length',data=data,kind='kde')