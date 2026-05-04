import pandas as pd
import numpy as np
a=pd.Series([5,6,7.8,9,np.nan,299.3],dtype=float)
#a.index #查看序列
#print(a.values)#查看值
a.index=list('abcdef')
# print(a["a":"d"])



