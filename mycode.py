import pandas as pd
import numpy as np 


df =  pd.read_csv("data/sample_data.csv")

df["grade"] = ["A","B" ,"C","A","B" ,"E","G" ,"B","A","C"]
print(df.to_csv('data/sample_data.csv', index=False))
