# 函数
# 定义函数 打印“---------------”
# def out_line():
#     print("-------------------------------------------")
# # 调用函数
# out_line()
# 计算圆的面积
# def circle_m(r):
#     m=3.14*r*r
#     return m
# print(circle_m(3))
# 计算长方形的面积
def cm(m,n):
    """
    计算长方形的面积
    :param m:长度
    :param n:宽度
    :return:返回长方形的面积
    """
    mian=m*n
    return mian
cm1=cm(3,4)
print(cm1)
help(cm)
# 计算圆的周长，半径（返回两个值）
# def circle(r):
#     return round( 3.14*r*r,1),round(3.14*r*2,1) # 保留一味小数
#  # 作为元组 解包
# area,length = circle(10)
# print(area)
# print(length)




