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
# a,b,c,d,e,f,g,h,i,j=students
#for k in students:
    #s, name, *num =k
    #omg=sum(num)/3
    #print(f"{name}的总分为{sum(num)},平均分为{omg:.1f}")
    #if omg>=90:
        #print(f"{name}，平均分为{omg:.1f}") #优秀学生

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
# 集合，不能存储重复的元素，set 集合，自动去重
# s1={1,6,9,5,6,75,7,74,79,89,84,8,2,4,5}
# print(s1)  # 为什么我输出后有序
# 定义空集合
# s=set() # 居然不是set{}
# s2={} # 注意这样定义出来的不是空集合，而是空字典
# print(type(s))
# print(type(s2))
# 集合的常见用法
# 1：add,添加元素
# s.add("ivti")
# s.add("till")
# print(s1)
# 2：remove,删除指定元素,只能删除一个元素啊。
# s.remove("till")
# print(s)
# 3: pop,随机删除元素并返回,返回的元素怎么写
# e=s1.pop()
# print(e)
# 4,5,6
# s2=(34,56,78,99,21,3,4,6,7)
# print(s1.difference(s2))        # difference求两个集合的差值，包含在第一个集合，但不在第二个集合 ==“-"
# print(s1.union(s2))          # union,合并两个集合 =="|"
# print(s1.intersection(s2))     # intersection求两个集合的交集 =="&"
# 8：clear,清空集合
# s.clear()   # 字符串可以用clear,int类型不行

# --------------------------------------------- 集合 set 案例 ---------------------------------------
# # 选修足球学生名单
# football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# # 选修篮球学生名单
# basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# # 选修法语学生名单
# french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# # 选修艺术学生名单
# art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
# # 1. 找出同时选修了 法语 和 艺术 的学生  french_set  art_set 并集，intersection
# print(french_set.intersection(art_set))
# # 方式2 ，&：求并集
# print(french_set & art_set)
#
# # 2. 找出同时选修了所有四门课程的学生,方式一
# b=french_set.intersection(art_set)
# c=b.intersection(football_set)
# d=c.intersection(basketball_set)
# print(d)
# # 方式2：
# print(football_set & basketball_set & french_set & art_set)
# # 3.找出选修了足球, 但是没有选修篮球的学生 - 差集
# print(football_set.difference(basketball_set))
# # 4. 统计每一个学生选修的课程数量
# a=football_set.union(basketball_set)
# a1=a.union(french_set)
# a2=a1.union(art_set)
# print(a2)
# # 求出了所有学生的姓名 并集：|: 还是去重了
# # l=[]
# # for i in football_set | basketball_set | french_set | art_set:
#     #l.append(i)
# all_list=[*football_set,*basketball_set,*french_set,*art_set]
# print(all_list) # 没去重的总人数
# for i in a2:
#     sum=all_list.count(i)
#     print(f"{i}参见了{sum}个项目")
# 字典，dict={key:value},和集合（set)一样，不能重复
# 注意，key为不可变类型，可以为，string,int,float以及tuple(元组)
# d1={"dazai":659,"chuya":700}
# d2={} # 空字典
# d3=dict()
# score=d1["chuya"]
# print(score)
# #修改value值
# d1["dazai"]=701
# 字典的常用操作
# d={"泡面":4,"火腿":2,"火锅":15,"酸汤面叶":3}
# d["冰淇凌"]=6 # 添加元素
# e=d.pop("火腿")
# del d["泡面"] # 删除字典的key
# print(d.keys())
# print(d.values())
# "崇祯五年的那场雪"
# dict 购物车案例
# d={}
# while True:
#     print("添加购物车,输入1")
#     print("修改购物车，输入2")
#     print("删除购物车，输入3")
#     print("查询购物车，输入4")
#     print("退出购物车，输入5")
#     choice=int(input("请输入数字1-5"))
# # 添加购物车
#     if choice==1:
#         name=input("输入商品名称")
#         if name in d:
#             print(f"{name}已经添加过了")
#         else:
#             price = input("输入商品单价")
#             count = input("输入商品数量")
#             d[name] = {"单价": price, "数量": count}
#     if choice==2:
#         name=input("输入要修改的商品名称")
#         if name not in d:
#             print(f"购物车里没有{name}，请按1去添加吧")
#         else:
#             new_price = input("输入新的单价")
#             new_count = input("输入新的数量")
#             d[name]["单价"] = new_price
#             d[name]["数量"] = new_count
#     if choice==3:
#         name=input("输入删除的商品名称")
#         if name not in d:
#             print(f"很抱歉，购物车没有{name}，删除不了")
#         else:
#             del d[name]
#     if choice==4:
#         if not d:
#             print("购物车是空的，快去添加吧")
#         for name,info in d.items():
#             print(f"商品名称为{name}，商品价格为{info["单价"]}，商品数量为{info["数量"]}")
#     if choice==5:
#         print("成功退出程序，欢迎下次再来")
#         break
# 购物车案例2，match.....case
# cart={}
# # 招牌
# a='''
# ################购物车系统##################
# #              1.添加商品名称              #
# #              2.修改商品名称              #
# #              3.遍历商品名称              #
# #              4.删除商品名称              #
# #              5.退出程序                 #
# ##########################################
# '''
# while True:
#     print("欢迎进入购物车系统")
#     print(a)
#     choice = int(input("请输入需要的数字"))
#     match choice:
#         case 1:
#             name = input("请输入需要添加的商品名称")
#             if name in cart:
#                 print(f"{name}在购物车已存在")
#             else:
#                 price = input("请输入商品单价")
#                 count = input("请输入商品数量")
#                 cart[name] = {"price": price, "count": count}
#         case 2:
#             name = input("请输入商品名称")
#             if name not in cart:
#                 print(f"很抱歉，购物车没有{name}，修改不了")
#             else:
#                 new_price = input("请输入新的价格")
#                 new_count = input("请输入新的数量")
#                 cart[name]["price"] = new_price
#                 cart[name]["count"] = new_count
#                 print(f"{name}的新价格为{new_price},新数量为{new_count}")
#         case 3:
#             if not cart:
#                 print("很抱歉，购物车为空，快去添加吧")
#             else:
#                 for name, info in cart.items():
#                     print(f"{name},价格为{info["price"]},数量为{info["count"]}")
#         case 4:
#             name = input("请输入商品名称")
#             if name not in cart:
#                 print(f"{name}不存在购物车，无法删除")
#             else:
#                 del cart[name]
#                 print("删除成功了")
#         case 5:
#             print("退出成功")
#             break
#         case _:
#             print("指令错误，请输入1-5之间的数字")
# 班级成绩管理系统
# student={}
# b='''
# ########### 班级成绩管理系统 #############
# #            1，录入成绩                #
# #            2，查询总分                #
# #            3，修改单科                #
# #            4，遍历字典                #
# #            5，退出系统                #
# ########################################
# '''
# while True:
#     print("欢迎来到班级成绩管理系统")
#     print(b)
#     choice=int(input("请输入你的选择"))
#     match choice:
#         case 1: # 录入成绩
#             name=input("请输入学生姓名")
#             if name in student:
#                 print(f"{name}学生已存在，请勿重复添加")
#             else:
#
#                 chinese=int(input("请输入该学生语文成绩"))
#                 math=int(input("请输入该学生数学成绩"))
#                 english=int(input("请输入该学生英语成绩"))
#                 total=chinese+math+english
#                 student[name]={"语文":chinese,
#                                "数学":math,
#                                "英语":english,
#                                "总分":total}
#                 print("录入成功")
#         case 2: # 查询总分
#             name = input("请输入学生姓名")
#             if name not in student:
#                 print("并未查询到该学生，请先添加")
#             else:
#
#                 print(f"该学生总成绩为{student[name]["总分"]}")
#
#         case 3: # 修改单科
#             name=input("请输入学生姓名")
#             if name not in student:
#                 print(f"{name}不在名单，无法修改")
#             else:
#                 print('''
#                 修改语文按1
#                 修改数学按2
#                 修改英语按3
#                 ''')
#                 sub=int(input("请输入要修改的学科数字"))
#
#                 match sub:
#                     case 1:
#                         new_chinese=int(input("请输入新的语文成绩"))
#                         student[name]["语文"]=new_chinese
#                         new_total=student[name]["语文"]+student[name]["数学"]+student[name]["英语"]
#                         student[name]["总分"]=new_total
#                         print("修改成功")
#                     case 2:
#                         new_math = int(input("请输入新的数学成绩"))
#                         student[name]["数学"] = new_math
#                         new_total=student[name]["语文"]+student[name]["数学"]+student[name]["英语"]
#                         student[name]["总分"]=new_total
#                         print("修改成功")
#                     case 3:
#                         new_english = int(input("请输入新的数学成绩"))
#                         student[name]["英语"] = new_english
#                         new_total=student[name]["语文"]+student[name]["数学"]+student[name]["英语"]
#                         student[name]["总分"]=new_total
#                         print("修改成功")
#                     case _:
#                         print("条件不匹配，重新输入")
#         case 4:
#             for name,info in student.items():
#                 avg=info["总分"]/3
#                 print(f"{name}，语文成绩：{info["语文"]}，数学成绩：{info["数学"]}，"
#                       f"英语成绩：{info["英语"]}，平均分:{avg:.1f}")
#         case 5:
#             print("成功退出系统")
#             break
#         case _:
#             print("指令出错，请输入1-5之间的数字")
# 简易通讯录
# add={}
# a='''
# ############欢迎进入通讯录系统###############
# #            1，添加联系人                 #
# #            2，模糊搜索                   #
# #            3，按分组查看                 #
# ##########################################
# '''
# while True:
#     print("欢迎来到通讯录系统")
#     print(a)
#     choice=int(input("请输入数字1-3"))
#     match choice:
#         case 1:
#             name=input("请输入联系人的姓名")
#             if name in add:
#                 print("该联系人已存在")
#             else:
#                 phone=input("请输入电话号码")
#                 address=input("请输入联系人的地址")
#                 group=input("请输入分组")
#                 add[name]={"phone":phone,"address":address,"group":group}
#                 print("添加成功")
#         case 2: # 遍历
#             name = input("请输入联系人的姓名")
#             if name not in add:
#                 print("查无此人")
#             else:
#                 print(f"{name},联系电话：{add[name]["phone"]},地址：{add[name]["address"]},分组：{add[name]["group"]}")
#
#         case 3:    # 按分组查看
#             group = input("请输入联系人的分组")
#             for name,info in add.items():
#                 if group==info["group"]:
#                     print(name,info["phone"])
#         case _:
#             break
# # 游戏背包系统
# backpack={}
# a='''
# ############ 游戏背包系统 #################
# ￥            1，捡装备                  ￥
# ￥            2，装备武器                ￥
# ￥            3，丢弃垃圾                ￥
# ￥            4，整理背包                ￥
# #########################################
# '''
# ma=0
#
# while True:
#     print("欢迎来到背包系统")
#     print(a)
#     choice=int(input("请输入你的选择"))
#     match choice:
#         case 1:   # 捡装备，添加
#             name=input("输入装备名称")
#             if name in backpack:
#                 print("该装备已存在，请勿重复添加")
#             else:
#                 type=input("请输入武器类型")
#                 attack=int(input("请输入攻击值"))
#                 dura=int(input("请输入耐久度"))
#                 backpack[name]={"type":type,"attack":attack,"dura":dura}
#                 print("添加成功")
#         case 2:   # 装备武器，修改
#             name = input("输入装备名称")
#             if name not in backpack:
#                 print("该武器不存在")
#             else:
#                 ma+=backpack[name]["attack"]
#                 new_dura=backpack[name]["dura"]-10
#                 backpack[name]["dura"]=new_dura
#                 print(f"主人的攻击力为{ma},武器的耐久度为{new_dura}")
#         case 3:    # 丢弃垃圾，删除
#
#             backpack={name:info for name,info in backpack.items() if info["dura"]!=0} # 循环中不能删除
#             print("耐久度为0的已删除")
#
#
#         case 4:  # 整理背包，遍历
#             for name,info in backpack.items():
#                 print(f"{name},攻击力：{info["attack"]},耐久度：{info["dura"]}")
#         case _:
#             break

# 欢迎来到教务管理系统
student={}
a='''
**************** 欢迎来到教务管理系统 ********************
*                 1，添加学生信息                       *
*                 2，修改学生信息                       *
*                 3，删除学生信息                       *
*                 4，查询学生信息                       *
*                 5，遍历学生信息                       *
*                 6，统计班级成绩                       *
*******************************************************
'''
while True:
    print(a)
    choice=int(input("请输入你的选择（1-6）"))
    match choice:
        case 1:
            name=input("请输入学生姓名")
            if name in student:
                print("该学生已存在，请勿重复添加")
            else:
                chinese=int(input("学生的语文成绩"))
                math=int(input("学生的数学成绩"))
                english=int(input("学生的英语成绩"))
                student[name]={"chinese":chinese,"math":math,"english":english}
                print("录入成功")
        case 2:
            name=input("请输入学生信息")
            if name not in student:
                print("系统中没有该学生")
            else:
                new_chinese=int(input("请输入新的语文成绩"))
                new_math=int(input("请输入新的数学成绩"))
                new_english=int(input("请输入新的英语成绩"))
#                 student[name]["chinese"]=new_chinese
#                 student[name]["math"]=new_math
                student[name]["english"]=new_english
                print("修改成功")
        case 3:
            name = input("请输入要删除的学生信息")
            if name not in student:
                print("系统没有该学生的信息")
            else:
                del student[name]
                print("删除成功")
        case 4:
            name=input("请输入要查询的学生信息")
            if name not in student:
                print("该学生信息不存在")
            else:
                print(student[name])
        case 5:
            for name,info in student.items():
                print(f"{name},语文：{info["chinese"]},数学：{info["math"]},英语：{info["english"]}")
        case 6: #  输出语文，数学，英语的最大值，最小值，以及平均值

            sum_chinese=0    #太麻烦了
            sum_math=0
            sum_english=0
            l1=[]
            l2=[]
            l3=[]
            for name,info in student.items():
               sum_chinese+=info["chinese"]
               sum_math+= info["math"]
               sum_english+= info["english"]
               l1.append(info["chinese"])
               a1=max(l1)
               a2=min(l1)
               l2.append(info["math"])
               b = max(l2)
               b1=min(l2)
               l3.append(info["english"])
               c= max(l3)
               c1=min(l3)
            name1={name for name,info in student.items() if info["chinese"]==a1}
            name2 ={name for name, info in student.items()if info["chinese"] == a2}
            name3 = {name for name, info in student.items() if info["math"] == b}
            name4 = {name for name, info in student .items()if info["math"] == b1}
            name5 = {name for name, info in student .items()if info["english"] ==c}
            name6= {name for name, info in student.items() if info["english"] ==c1}
            print(f"语文的最高分为{a1},是{name1}同学,最低分为{a2},是{name2}同学，平均分为{sum_chinese/len(student):.1f}")
            print(f"数学的最高分为{b},是{name3}同学，最低分为{b1},是{name4}同学，平均分为{sum_math /len(student):.1f}")
            print(f"英语的最高分为{c},是{name5}同学，最低分为{c1},是{name6}同学，平均分为{sum_english /len(student):.1f}")
        case _:
            break











































































































