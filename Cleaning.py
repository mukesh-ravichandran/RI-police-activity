import pandas as pd
ri= pd.read_csv("police.csv")
ri.head()
ri.isnull().sum() 
print(ri.shape) 
ri.drop(['county_name', 'state'], axis='columns', inplace=True)
print(ri.shape)





