import pandas as pd
import numpy as np 

#import datas
data=pd.read_csv("input/train.csv")

#preview
print(data.head(5))

#count 
print(f"{len(data)}rows")
print(data.columns)

#see Survived data
data_survived=data[data["Survived"]==1]
count_survived=len(data_survived)
data_not_survived=data[data["Survived"]==0]
count_not_survived=len(data_survived)
print(data_survived,count_not_survived)

#output data
data_survived.to_csv("output/survived.csv")
data_not_survived.to_csv("output/survived.csv")
