import pandas as pd
import os

data={
    'Name':['Aman','Anand','Ashish'],
    'Age':[23,34,33],
    'City':['Mumbai','Pune','Nasik']
}

df=pd.DataFrame(data)

#Adding new row in Dataframe v2
new_row={'Name':'Honey','Age':21,'City':'Indore'}
df.loc[len(df.index)]=new_row

#Make Dir
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'Sample1.csv')

df.to_csv(file_path,index=False)

print(f"File save at path : {file_path}")



