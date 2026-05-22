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
# def cm(m,n):
#     """
#     计算长方形的面积
#     :param m:长度
#     :param n:宽度
#     :return:返回长方形的面积
#     """
#     mian=m*n
#     return mian
# cm1=cm(3,4)
# print(cm1)
# help(cm)
# 计算圆的周长，半径（返回两个值）
# def circle(r):
#     return round( 3.14*r*r,1),round(3.14*r*2,1) # 保留一味小数
#  # 作为元组 解包
# area,length = circle(10)
# print(area)
# print(length)
# 计算三角形的面积
# def triangle_area(bottom,tall):
#     '''
#     计算三角形的面积
#     :param bottom: 底
#     :param tall: 高
#     :return: 返回三角形的面积
#     '''
#     area=bottom*tall/2
#     return area
# bottom=int(input("底"))
# tall=int(input("高"))
# print(triangle_area(bottom,tall))
# def count_vowel(s):
#     """
#     计算传入的字符串中元音字母的个数
#     :param s: 字符串
#     :return: 返回字符串的个数
#     """
#     s_vowel="aeiouAEIOU"
#     count=0
#     for i in s:
#         if i in s_vowel:
#             count+=1
#     return count
# s=input("请输入字符串")
# print(count_vowel(s))
# def a (score):
#     big=max(score)
#     small=min(score)
#     avg=round(sum(score)/len(score),1)
#     return big,small,avg
# class_score=[234,567,789,345,124,345,323]
# big,small,avg=a(class_score)
# print(f"最高分是{big}")
# print(f"最底分是{small}")
# print(f"平均分是{avg}")
# def reg_stu(name,age,gender,city):
#     print(f"注册成功，姓名{name}，年龄{age}，性别{gender}，城市{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
# # 位置传参
# stu1=reg_stu("张三",23,"男","北京")
# print(stu1) #  返回两行
# # 关键字传参：关键字顺序无所谓
# stu2=reg_stu(name="梨花",city="上海",age=17,gender="女")
# print(stu2)
# # 位置混合关键字传参:关键字必须在后
# stu3=reg_stu("小敏",32,city="无锡",gender="女")
# print(stu3)
# # 默认参数
# def re(name,age,gender="女",city="北京"):
#     print(f"注册成功，姓名{name}，年龄{age}，性格{gender}，城市{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
# print(re("云华",45))
# def cm(num):
#     ma=max(num)
#     mi=min(num)
#     avg=round(sum(num)/len(num),1)
#     return ma,mi,avg
# num=[]
# i=0
# while i<=5:
#     i+=1
#     num1=int(input("请输入数字"))
#     num.append(num1)
# ma,mi,avg=cm(num)
# print(f"最大值{ma}")
# print(f"最小值{mi}")
# print(f"平均值{avg}")
# 定义函数，根据传入的数据，计算这批数据中的最大值，最小值，平均值
# def calc_data(a,b,c,d):
#     ma=max(a,b,c,d)
#     mi=min(a,b,c,d)
#     avg=round((a+b+c+d)/4,1)
#     return ma,mi,avg
# ma,mi,avg=calc_data(23,56,78,45)
# print(f"最大值{ma}")
# print(f"最小值{mi}")
# print(f"平均值{avg}")
# 不定长参数----位置传递(*args)
# 不定长参数，关键字参数 **kwarg
# def clca_num(*args,**kwargs):
#     ma=max(args)
#     mi=min(args)
#     avg=sum(args)/len(args)
#     if kwargs.get("round"):
#         round(avg,kwargs.get("round"))
#     print(kwargs)
#     return ma,mi,avg
# ma,mi,avg=clca_num(11,22,33,44,55,66,77,88,99,round=2,count=0)
# print(ma)
# print(mi)
# print(avg)
# def info(**kwargs):
#     print(type(kwargs))
#     print(f"内容是{kwargs}")
# info(name="小米",age=36,gentle="男",city="武汉")
# 当参数作为函数
# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def calc(x,y,oper):
#     return oper(x,y)  #  oper作为函数调用,调用时填写上面函数名
# result=calc(32,56,subtract)
# print(result)
# 匿名函数 lambda 参数，函数体 .注意，函数体是单行表达式
# def out_line():
#     print("----------")
# out_line()
# out_lint=lambda :print("-------")
# out_lint()
# #定义一个加法
# def add(x,y):
#     return x+y
# print(add(4,7))
# #lambda 写法
# add1=lambda x,y:x+y
# print(add1(7,7))
# 完成以下列表的排序操作，按照每一个元素的字符个数，从小到大排序
# data_list=["c++","c","python","jack","php","java","go","javascript","rust"]
# def sort_list(x):
#     co=[]
#     for i in x:
#         sum=len(i)
#         co.append(sum)
#     return sorted(co)
# print(sort_list(data_list))
# def sort_list1(x):
#     return sorted(x,key=len,reverse=True) # key=len,表示按照元素的长度排序
# print(sort_list1(data_list))
# 定义一个函数，根据传入的数字，计算该数字阶乘的结果
# def factorial(x):
#     mul=1
#     for i in range(1,x+1):
#         mul*=i
#     return mul
# x=int(input("请输入你的数字"))
# result=factorial(x)
# print(result)
# 递归调用，数字阶乘
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return x*factorial(x-1) # 自己调用自己，当x=1,返回1，不再进行调用
# result=factorial(int(input("请输入数字")))
# print(result)
def total_price(product,coupon,discount,fee):



























































