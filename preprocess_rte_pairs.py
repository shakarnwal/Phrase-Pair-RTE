import numpy as np
import pandas as pd

with open ("natlog-labeled-rte-pairs.txt", "r") as myfile:
    data = myfile.readlines()

data1 = data[1:]
data2 = [i.split('.0', 1)[0] for i in data1]

cleaned_data = []
for row in data2:
    newrow = []
    newrow.append(row.split('\t',3)[0])
    newrow.append(row.split('\t',3)[1])
    newrow.append(row.split('\t',3)[2])
    cleaned_data.append(newrow)    

cleaned_data.insert(0,['truth','hypothesis','majority_label'])

headers = cleaned_data.pop(0)

df = pd.DataFrame(cleaned_data, columns=headers)

df = (df[~(df["majority_label"] == 'none')])
df = (df[~(df["majority_label"] == 'NA')])

df.to_csv('phrase_pair_entailment.csv',index=False)
