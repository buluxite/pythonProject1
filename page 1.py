"""
多行注释只有第一行是灰色的
（桀桀桀）
"""

"""
print(666)
print("printf")
print("c乱入")
"""
#学了一点c,又回来学python，发现忘的差不多了
# 单行注释（加个空格就没有波浪线了）
# 多行注释（在#号和内容之间加空格）
"""
print(4599)
print(2740)
"""
"""
#变量直接写，不需要写int money =50
money=50
print(money)
cake=7
money=money-cake
print("钱包还有:",money)
#假设每隔一小时，钱包的余额增加10元
money=99
print("下午一点，钱包余额为:",money)
print("下午二点，钱包余额为:",money+10)
money=money+10
print("下午三点，钱包余额为:",money+10)
"""
"""
#type查看数据类型
a=type(666)
print(a)
print(type(13.33))
print(type(""))
"""
#数据类型的转换
#int(x)
#float(x)
#str(x)
"""
print(int(13.14))
#print(int("三星"))
#字符串汉字无法转换为整数
print(float(12))
#print(float("七星"))
#同理，字符串汉字也无法转换为浮点数
print(str(13.14))
print(str(45))
"""
# 输出单引号，外面用双引号
# 输出双引号，外面用单引号
"""
print("'黑马程序员'")
print('"黑马"')
# 转义字符（右下斜杠）：无视后面符号

"""
"""
#字符串的拼接，+号。注意：只有字符串可以进行拼接，数字(整数和浮点数)不可以拼接
day="周一"
thing="15元"
print(day+"花了"+thing+"吃饭")
money=str(17.6)
print(day+"花了"+money+"元")
print ("%s吃饭花了%s,喝了杯奶茶，花了%s"%(day,thing,money))
#字符串 %s
#整数 %d
#浮点数 %f
#浮点数精度的控制，m.n=156.945.(m=3,n=3) %3.3f 控制到%3.2f
#m可以省略，写成%.2f
a=156.945
print("总价为%.2f" %a)
"""
# num=input("请在键盘上输入一个数")
# n=int(num)
# #键盘上录入的数字都是字符串类型，需要转换为数字类型
# #判断键盘上的数字是否大于20，小于100
# if n>=20 and n<=100:
#     print(f"{n}大于20并且小于100")
# else:
#     print(f"{n}不在20到100之间")
# #if.....else.....
#全部注释ctrl+/
#根据用户输入的年份，判断是否是闰年。
#闰年，如果被400整除，为闰年
#如果不能被100整除，能被4整除，则也为闰年
# num=input("请输入数字的年份")
# n=int(num)
# if n%400==0:
#     print(f"{n}年是闰年")
# elif n%100!=0 and n%4==0:
#     print(f"{n}年是闰年")
# else:
#     print(f"{n}年不是闰年")
#需求1，判断用户输入的数字是奇数还是偶数
# num=int(input("请输入一个数字"))
# if num%2==0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}不是偶数")
#需求2，判断用户输入的数字是正数还是负数
# num=int(input("请输入一个数字"))
# if num>0:
#     print(f"{num}是正数")
# elif num<0:
#     print(f"{num}是负数")
# else:
#     print("这个数是0")
# 根据输入三条边是边长，判断是等边三角线，等腰三角形，还是直角三角线
# a=int(input("输入第一条边的边长"))
# b=int(input("输入第二条边的边长"))
# c=int(input("输入第三条边的边长"))
# if a+b>c and a+c>b and b+c>a:#任意两条边要大于第三条边（不能用or)
#     print("能构成三角形")
#     if a==b==c:
#         print(f"{a},{b},{c}组成的是等边三角形")
#     elif a==b or a==c or b==c:
#         print(f"{a},{b},{c}组成的是等腰三角形")
#     elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a :
#         print(f"{a},{b},{c}组成的是直角三角形")
#     else:
#         print(f"{a},{b},{c}组成的是普通三角形")
#
# else:
#     print(f"{a},{b},{c}不能组成三角形")
# app=input("请输入你要打开的app")
# #match...case
# match app:
#     case "github":
#         print("推送代码")
#     case "bilibili":
#         print("追番")
#     case "淘宝":
#         print("买谷子")
#     case "原神":
#         print("打游戏")
#     case "抖音" :
#         print("续火花")
#     case _:
#         print("输入错误")
# 停止键是？(default?)其他怎么算？（else==case_)
#实现一个计算机，进行加减乘除运算
# a=int(input("请输入第一个数字"))
# b=int(input("请输入第二个数字"))
# c=input("请输入加减乘除的运算符")
# match c:
#     case "+":
#         print(f"{a}+{b}的结果是{a+b}")
#     case "-":
#         print(f"{a}-{b}的结果是{a-b}")
#     case "*":
#         print(f"{a}*{b}的结果是{a*b}")
#     case "/" if b!=0:   # case后面加条件判断
#         print(f"{a}/{b}的结果是{a/b}")
#     case _:
#         print("对不起，没找到匹配的运算符")
#while循环
# i=0
# while i<10:
#     i+=1
#     print("对不起啊，老齐，笨鸟没做到诸般困厄已前尘")
# else:
#     print(f"等一等，第{i+1}次，来日青与清溪长")
# 计算1-100之间，所有偶数的累加之和
# i=1
# sum=0
# while i<=100:
#     i+=1
#     if i%2==0:
#         sum+=i
#         print(f"当i等于{i},sum={sum}")
# a="没钱买周边了，(悲)"
# n=0
# #for循环
#
# for i in a:
#     n+=1
#     print(f"第{n}个是{i}")
# else:
#      print("循环结束")
#计算1-100之间，所有奇数之和.for(?,1到100怎么表示？)
#range语句，range(2,8)
#获取的数据是从2到7 注意不包含end,即8
# sum=0
# for i in range(1,100):
#     if i%2!=0:
#         sum+=i
#         print(f"当i等于{i},sum={sum}")
# else:
#     print("循环结束")  sum==2500
#计算100到500之间，所有三倍数的数字之和，for.
# sum=0
# for i in range(100,500):
#     if i%3==0:
#         sum+=i
# print(f"当i等于{i},sum={sum}")#  sum=39900
# 打印一个长度为m,宽度为n的长方形，嵌套循环，两个循环
# m=int(input("请输入长方形的长度"))
# n=int(input("请输入长方形的宽度"))
# for j in range(n):
#     print("\n")   # 换行没想到
#     # print默认换行，end=""取消换行
#     for i in range (m):
#         print("*",end=" ")
#打印九九乘法表
# for i in range(1,10):
#     print()
#
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}",end="  ")#瞎写的云云，其实我也不懂，、。。。。
#根据输入的直角边的边长，打印等腰直角三角形
# i=int(input("请输入直角边的边长："))
# for i in range(i):
#     print()
#     for j in range(i+1):
#         print("*",end="\t")
#打印对应的金字塔
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
"""
# a=int(input("请输入数字："))
# for i in range(a):
#     print()
#     for j in range(i+1):
#         print(j+1,end=" ")
# 依然不知道在写什么，反正调试调试就出来了
# 打印国际象棋盘
# for i in range(6):
#     print()
#     for j in range(6):
#         if j%2==0:
#             print("▬",end=" ")
#         else:
#             print("▭",end=" ")
# 根据输入的账号密码进行登录
# a=input("请输入您的账号")
# b=input("请输入您的密码")
# false = a!="admin" or b!="66688"
# true  = a=="admin" and b=="66688"
# #校验输入的用户名和密码不能为空
# if a=="" or b=="":
#     print("注意用户名和密码不能为空")
#
# if true:
#     print("成功登录")
# while false:
#     print("账号或密码错误，请重新登录")
#     a = input("请输入您的账号")
#     b = input("请输入您的密码")
#     false = a != "admin" or b != "66688"
#     true = a == "admin" and b == "66688"
#     if a == "" or b == "":
#         print("注意用户名和密码不能为空")
#
#     if true:
#         print("成功登录")
# 好丑的代码，云云，也是能跑就行
# while True:
#
#     s=input("睡美人会醒来在几时？：")
#     f=input("睡美人会醒来在几分")
#     if s=="" or f=="":
#         print("不可以输入空字符喔~")
#         continue
#     if s=="18"and f=="22":
#         print("恭喜你，公主醒啦，你就是命定的骑士")
#         break
#     else:
#         print("很抱歉，公主并未苏醒")
#         print("请再输入一遍吧")
# 猜数字游戏，系统随机生成随机数
# import random
# number=random.randint(1,10)
# while True:
#     a=int(input("请输入一个1到10以内的随机数"))
#     if a=="":
#         print("禁止输入空字符")
#         continue
#     if a==number:
#         print("恭喜猜对了")
#         break
#     elif a<number:
#         print("猜小了")
#
#     elif a>number:
#         print("猜大了")
#列表
a=[2,7,8,90,54,67,89,3,2,16,78,89,66,True,"python"]
#获取列表里的数据
# print(a[0])
# print(a[-1])
#修改列表里面的数据
# a[-3]=False
# print(a[-3])
# print(a)
#删除列表中的数据
# del a[0]
# print(a)
#遍历列表
for i in a:
    print(i)




































