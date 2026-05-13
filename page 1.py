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
# a=[2,4,5,6,7,8,9,3,34,56,"python",True]
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
# for i in a:
#     print(i)
# 对列表进行切片操作
# a=[23,56,79,0,True,"fate",23.89,False]
# # b = a[0:5] # [开始索引：结束索引：步长]注意；截取后的结果不包含结束索引
# #
# # print(a[4:9])
# # # 列表的常见方法
# a.append(79) # 在列表尾部添加元素,只能添加一个元素吗？
# # a.insert(1,666) # 在列表指定元素前面添加元素，注意是前面
# print(a)
#
# a.remove(79) # 删除列表中第一个匹配到的值，remove,后面写的是列表的值
# a.pop(3) #删除列表中指定索引的值，pop,后面括号里面写是列表的索引
# print(f"列表a为{a},在列表a后面添加一个元素666,变成{a.append(666)}，\n在fate后面添加一个元素eva,"
#       f"列表a变成{a.insert(5,"eva")},\n删除列表a的元素0，列表a变成{a.remove(0)
#       },\n删除列表a的最后一个元素，列表a变成{a.pop()}")
# {}里面的值用不了？！！！

# c=[1,56,87,34,56,83,42,56,34,77,663,45]
# c.sort() #对列表的元素进行排序，注意：列表元素一致才可以排序
# print(c)
# a.reverse()
# c.reverse()
# print(a)
# print(c)
# 对c中的元素进行排序,输出其中的最大值，最小值和平均值
# sum=0
# k=0
# for i in c:
#     k+=1
#     sum+=i
# print(sum/k)# 列表c的平均值
# c.sort()# 从小到大排
# print(c)
# e=c.pop(0)
# print(e)#最小值
# c.reverse()
# e=c.pop(0)
# print(e)#最大值
# #定义列表？怎么定义一个列表，so?,定义了一个空列表
# a=[]
#将用户输入十个数字输入到列表中,注意空格会报错
# for i in range(10):
#     n=int(input("请输入数字"))
#     a.append(n)
# print(a)
# a.sort()
# print(f"列表a的最小值{a[0]}")
# a.reverse()
# print(f"列表a的最大值{a[0]}")
# print(f"列表a的平均值{sum(a)/len(a)}")# len计算列表长度
# print(min(a))
# print(max(a))
# a=[19,23,54,64,875,20,109,232,123,54]
# b=[55,80,72,35,60,123,54,23,91]
# print(a.append(b))# 运行不了，用for循环,合并列表
# for i in b:
#     a.append(i)
# print(a)
# #去除重复元素
# new=[]
# for i in a:
#
#     if i in new:
#         new.remove(i)
#     new.append(i)
# print(new)
#简化合并列表 ,+666
# c=a+b
# print(c)
# #简化合并列表3，解包
# c=[*a,*b]
# print(c)
#生成1-20的平方列表
# a=[]
# for i in range(1,21):
#     c=i*i
#     a.append(c)
# print(a)
#提取所有偶数，并计算其平方，组成新的列表
# list1=[]
# for i in a:
#     if i%2==0:
#         l=i*i
#         list1.append(l)
# print(list1)
# # 简洁的方法生成1-20的平方列表，列表推导式：[需要的数据 for i in (序列/列表）]
# new=[i*i for i in range(1,21)]
# print(new)
# # #提取所有偶数，并计算其平方，组成新的列表,列表推导式2：[需要的数据 for i in (序列/列表) if 条件]
# new2=[i**2 for i in new if i%2==0]
# print(new2)
#定义列表
# a=[]
# #定义字符串
# b=""
# s="Hello sariel"
# # s1="今天半夜吃不吃冰淇凌？"
# # #字符串的切片
# # print(s[5:15])
# # print(s1[2:10])
# # 字符串的常用方法
# print(s.find("sariel")) # 返回第一个s的索引位置
# print(s.count("l")) # 计数，计算l在字符串出现的次数
# print(s.upper()) # 将字符串转化为大写
# print(s.lower()) # 将字符串转化为小写
# print(s.strip("l")) # 啥叫去掉指定字符啊？，去掉开头和结尾的字符，包括去掉字符串开头和结尾的空字符串
# # 这个有点奇怪，能去掉开头”H“和结尾的”了“，去不掉中间的字符，比如”e“。
# print(s.replace("Hello","2740"))
# print(s.startswith("H")) # 为什么替换成了“2740”，原字符串还是以“Hello"开头
# # 因为字符串不可变，列表可以变
# print(s.split(" ")) # 将字符串按指定的分隔符分割成列表
# 邮箱格式验证
# while True:
#     s=input("请输入你的邮箱：")
#     a=s.count("@")
#     b=s.count(".")
#     if a==1 and b>=1:
#         print("邮箱格式正确")
#         break
#     else:
#         print("邮箱格式不正确")
# 邮箱验证方式2：if "...."  in 字符串
# while True:
#     a=input("请输入您的邮箱")
#     if "@" in a:
#         print("格式正确")
#         break
#     else:
#         print("格式错误")
# 判断输入的字符串是否是回文，eg:"黄山落叶松叶落山黄”，
# str=input("请输入字符串")
# if str==str[::-1]:
#     print(f"{str}是回文")
# else:
#     print(f"{str}不是回文")
# 将用户输入的十个字符串全部反转，并转化为大写，记录到列表中，并遍历输出
# a=[]
# for i in range(10):
#     str=input("输入字符串")
#     str1=str[::-1]
#     a.append(str1.upper())
# print(a)
# for i in  a:
#     print(i)
# 元组不可改变
# t1=(23,56,3,4,5,6,7,8,9,22,2,11,11,111,11,11,1,11,11,11)
# #空元组
# t2=()
# t3=tuple()
# print(t1.count(11))  # 计数11出现的次数
# print(t1.index(23))   # 计算元素出现是索引位置
# print(t1[2])
# print(t1[2:9])  #  同样不包括最后一个元素
# # t1[0]=100 #元组不支持赋值操作
# t=(3,6,7,9,3)
# #解包
# a,*b,c=t
# print(*b)
# print(b)   # 列表形式
# 将两个变量交换 ,纯交换
# a=10
# b=20
# # c=a
# # a=b
# # b=c
# # print(a)
# # print(b)
# # 用列表 交换
# t=(a,b)
# b,a=t
# print(a)
# print(b)
#交换三个数的值
# a=100
# b=200
# c=300
# # t1=(a,b,c)
# # c,a,b=t1
# #优化
# c,a,b=a,b,c
# print(c,a,b)
"""
    根据如下提供的学生成绩单，完成如下需求：
        1. 计算每个学生的总分、各科平均分，然后一并输出出来。
        2. 统计各科成绩的最低分、最高分、平均分，并输出。
        3. 查找成绩优秀（平均分大于90）的学生，并输出。
"""
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)
# 错误 ,用for循环，不用写+=1
a,b,c,d,e,f,g,h,i,j=students
for k in students:
    s, name, *num =k
    omg=sum(num)/3
    #print(f"{name}的总分为{sum(num)},平均分为{omg:.1f}")
    if omg>=90:
        print(f"{name}，平均分为{omg:.1f}") #优秀学生

# print("_______________________________________________________________________________________-")
# 方式1，用下标写
# for s in students:
#     total=s[2]+s[3]+s[4]
#     avg=total/3
#
#     print(f"{s[1]}的总成绩为{total}，平均分为{avg:.1f}") #为啥是:.1f
# 2. 统计各科成绩的最低分、最高分、平均分，并输出。
# chinese=[]
# math=[]
# english=[]
# for i in students:
#     s,name,chinese1,math1,english1=i
#     chinese.append(chinese1)
#     math.append(math1)
#     english.append(english1)
# print(f"语文最高分为{max(chinese)},最低分为{min(chinese)},平均分为{sum(chinese)/10}")
# print(f"数学最高分为{max(math)},最低分为{min(math)},平均分为{sum(math)/10}")
# print(f"英语最高分为{max(english)},最低分为{min(english)},平均分为{sum(english)/10}")
# 3. 查找成绩优秀（平均分大于90）的学生，并输出。








































































