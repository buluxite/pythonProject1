#使用直方图
#绘制三次

from matplotlib import pyplot as plt
plt.rcParams["font.family"]=["sans-serif"]
plt.rcParams["font.sans-serif"]=["SimHei"]

#战狼2三天的数据
x1=range(1,4)#天数三天
y1=[23,45,34]#三天的票房数

x2=range(7,10)
y2=[23,56,33]

x3=range(13,16)
y3=[34,56,24]
plt.figure(figsize=(16,8),dpi=65)
plt.bar(x1,y1)
plt.bar(x2,y2)
plt.bar(x3,y3)
x=list(x1)+list(x2)+list(x3)
a=["战狼2","黑神话悟空","崩铁星穹铁道"]
plt.xticks(x[::3],a)
plt.xlabel("片名")
plt.ylabel("票房数")
plt.grid(alpha=0.4)
plt.show()



