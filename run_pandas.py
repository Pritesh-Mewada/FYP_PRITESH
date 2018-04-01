import pandas as pd
import numpy as np


np.set_printoptions(threshold=np.nan)

df = pd.read_csv('cowrieLoginSuccess.csv')
mat =df.values

modified_col=[]
for i in mat:
    x=list(i)
    string =i[7]
    a = string.index('[')
    m = string.index('/')
    e = string.index(']')
    x.append(string[a+1:m])
    modified_col.append(x)
fd = pd.DataFrame(modified_col)
fd.to_csv("Cowrie_Login_Modified.csv")