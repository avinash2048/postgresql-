import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

#import data
data=pd.read_csv("input/train.csv")
#statistics
print(data.describe())

#info
print(data.info())

#visualize
# sns.pairplot(data.head())
# plt.show()

# sns.distplot(data["Age"].dropna())
# plt.show()

# fig=plt.figure(figsize=(6,6))
# sns.heatmap(data.corr(),annot=True)
# plt.show()

# data["Fare"].plot.(grid=True)
# data["Fare"].plot.bar(grid=True)
data[["Fare"]].head(20).sort_values(by="Fare",ascending=False).plot.pie(grid=True,subplots=True)
plt.show()