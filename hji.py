#import numpy as np
# t1=np.arange(3,89,5)
# print(t1.dtype)
# t2=np.array([[1,2,3],[5,6,7]])
# print(t2.shape)
# t4=np.arange(15)
# print(t4.reshape(3,5))
#t5=np.arange(24).reshape(4,3,2)

#四块三行两列
# print(t5)
# t6=t5.reshape(1,24)
# print(t6)
# t5.flatten()
# t6=np.arange(6).reshape(3,2)
# print(t6)
#三行两列
#
#取第三行的数字
# print(t5)
# print("*"*50)
#取第三行第五列的数字
#取二到四行，二到五列的数据
#取连续的多行,取2到4行
#print(t5[[1,2,3],:])
#取连续的多列.取第二至多列
#print(t5[:,1:])
#改值
#print(np.where(t5<10,0,10))
# t6=np.where(t5>19,5,15)
# print(t6)
#print(t5.clip(10,17))
"""
from matplotlib import  pyplot as plt

import pandas as pd
import tushare as ts
# 初始化pro接口
pro = ts.pro_api('23dadde75b2d7edceca6e4fb497cc5ae391de088b4e8724eec447f1d')
# 拉取数据
df= pro.daily(
    ts_code="600000.SH",start_date="20231101",end_date="20231202")
df=df.loc[:,["trade_date","open","high","low","close","vol"]]

#转换日期的格式
df["Date"]=pd.to_datetime(df["trade_date"])
df.set_index(["Date"],inplace=True)#将时间作为行
df=df.sort_index()#时间正序
    #绘图
plt.title("600000.SH")
plt.xlabel("time")
plt.ylabel("price")
plt.plot(df["open"],"bo-")
plt.plot(df["close"],"bo-")
plt.show()
#删除缺失值
stock_price=df["close"]
stock_price=stock_price.dropna()
#计算日收益率
Pt=stock_price
Pt1=stock_price.shift(1)
rt=Pt/Pt1
day=np.log(rt)
day_mean=day.mean#日均收益率
year=day_mean*252
#日波动率
day_bo=day.std()
year_bo=day_bo*np.sqrt(252)
print(year)
"""
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('23dadde75b2d7edceca6e4fb497cc5ae391de088b4e8724eec447f1d')

# 拉取数据
df = pro.daily(
    ts_code="600837.SH",

    start_date="20231101",
    end_date="20231202")

df=df.loc[:,["trade_date","open","close","high","vol"]]
#转换日期
df["Date"]=pd.to_datetime(df["trade_date"])
df.set_index(df["Date"],inplace=True)
df=df.sort_index()
print(df.head())
#画图
plt.plot(df["close"],"r+")
plt.plot(df["open"],"b-")
plt.xlabel("time")
plt.ylabel("price")
plt.title("600837.SH")
plt.show()
#计算日利率
a=df["close"]
a1=a.shift(1)
b=np.log(a/a1)
day=b.mean()
year=day*252
print(year)
"""
# import numpy as np
# a=np.array([3,6,8,9,26])
# a1=a[1:]
# a2=a[:4]
# print(a1-a2)
# from matplotlib import pyplot as plt
# import pandas as pd
# import numpy as np

# 导入tushare
# import tushare as ts

# 初始化pro接口
# pro = ts.pro_api('23dadde75b2d7edceca6e4fb497cc5ae391de088b4e8724eec447f1d')

# 拉取数据
# df = pro.daily(
#     ts_code="600678.SH",
#
#     start_date="20231101",
#     end_date="20231203")
#
# df=df.loc[:,["trade_date","open","high","close","vol"]]
#转换日期格式并正序
# df["Date"]=pd.to_datetime(df["trade_date"])
#将trade_date作为第一列
# df.set_index(df["Date"],inplace=True)
#将第一行正序
# df=df.sort_index()
# print(df.head())
#画图
# plt.figure(figsize=(20,8),dpi=80)
# plt.plot(df["close"],"r")
# plt.plot(df["open"],"y")
# plt.plot(df["close"],"r+")
# plt.plot(df["open"],"b-")
# plt.xlabel("date")
# plt.ylabel("price")
# plt.grid(alpha=0.3)
#plt.show()
#计算年利率
# a=df["close"]
# b=a.shift(1)
# c=np.log(a/b)
# day_=c.mean()
# year=day_*252
# print(year)
# a=df["close"]
# a1=a.shift(1)
# b=np.log(a/a1)
# day=b.mean()
# year=day*252
# print(year)
import numpy as np
# a=np.array([20,2,4,6,7])
# b=np.where(a<10)
# print(a[a>10])
#print(b)
c=np.arange(3,36).reshape(3,11)
a=np.array([1.9,4],dtype=float)
print(a)























