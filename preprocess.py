# coding=utf-8
import pandas as pd

obj = pd.read_csv("./Building_Permits.csv")
attr=[]
file = open("./count_file_50.txt",'w+')
for item in obj.columns:
    n = obj[item].value_counts()
    if n.count() < 50:
        attr.append(item)
        file.write("%s\t %d\n" %(item,n.count()))
file.close()
df = obj[attr]
df.to_csv("./t_50.csv",index=False,header=False)






