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
a=int(input("输入第一条边的边长"))
b=int(input("输入第二条边的边长"))
c=int(input("输入第三条边的边长"))
if a+b>c and a+c>b and b+c>a:#任意两条边要大于第三条边（不能用or)
    print("能构成三角形")
    if a==b==c:
        print(f"{a},{b},{c}组成的是等边三角形")
    elif a==b or a==c or b==c:
        print(f"{a},{b},{c}组成的是等腰三角形")
    elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a :
        print(f"{a},{b},{c}组成的是直角三角形")
    else:
        print(f"{a},{b},{c}组成的是普通三角形")

else:
    print(f"{a},{b},{c}不能组成三角形")











