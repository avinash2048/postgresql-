import pandas as pd 
from sqlalchemy import create_engine ,types
import json
#extract data
data =pd.read_csv("input/train.csv")
#transform data

#load data
engine=create_engine("postgresql://postgres:Orange1$#@localhost:5432/Train")
data["test"]=json.dumps({'key1':'value1','key2':'value2'})
data["test"]=data["test"].apply(lambda x: json.loads(x))
data.to_sql("Train",engine,index=False,if_exists="replace",dtype={"test":types.JSON})
print("inserted to database")
