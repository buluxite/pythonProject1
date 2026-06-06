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
# 计算最后的商品的总价，需要：参数
# 1，商品列表（商品名称，商品单价，商品数量）
# 2，优惠劵金额
# 3，积分数量
# 4，运费
# def calculate_order_total(items,coupon,points,shipping):
#     pass
# # 1，计算商品总价
# total=0
# items={}
# # 变量 items
# name=input("请输入商品名称")
# if name in items:
#     print("该商品已存在，请勿重复添加")
# else:
#     price=int(input("请输入商品价格"))
#     count=int(input("请输入商品数量"))
#     items[name]={"price":price,"count":count}
# for i in items.items():
#     total1=items["price"]*items["count"]
#     total+=total1
# print(total)
# # 2,优惠劵
# coupon=int(input("请输入优惠劵的数额"))
# if coupon>total:
#     print("优惠金额不可超过总价")
# else:
#     if total>=5000:
#         print("优惠劵满足条件，可以使用")
#         total =total-coupon
#     else:
#         print("商品金额满5000才能使用优惠劵")
# # 3，积分折扣
# if total >5000:
#     print("可以使用")
#     points=int(input("请输入积分金额"))
#     if points / 100!=0:
#         b=points/100
#         total=total-b
#     else:
#         print("抱歉，积分只能整百抵扣")
# else:
#     print("不可使用")
# # 4,运费
# shipping=int(input("请输入运费"))
# total=total+shipping
# def calculate_order_total(items,coupon,points,shipping):
#     total=0
#     for i in items:
#         total+=i["price"]*i["count"]
#     print(f"商品的价格为{total}")
#     # 计算优惠，coupon
#     if coupon>total:
#         print("不好意思，优惠不能超过单价")
#     else:
#         if total>=5000:
#             total=total-coupon
#             print(f"优惠后的价格是{total}")
#         else:
#             print("商品总价没有5000，不给予优惠")
#     # 计算折扣，points
#     if total>=5000:
#         if points>total:
#             print("折扣金额不能超过商品单价")
#         else:
#             if points//100!=0:
#                 b=points//100
#                 total=total-b
#                 print(f"打折后的价格为{total}")
#             else:
#                 print("积分不够整百，不能抵扣")
#
#     else:
#         print("商品的总金额没达到5000，不给予使用积分卡")
#     # 运费
#     total+=shipping
#     print(f"最后的价格为{total}")
#     return total
# items=[{"name":"苹果","price":1000,"count":3},
#        {"name":"西瓜","price":2000,"count":1},
#        {"name":"草莓","price":1000,"count":2}]
#
# calculate_order_total(items,1000,67800,500)
# 电商订单计算器
# def calculate_order_total(items,coupon,points,shipping):
#     total=0
#     for i in items:
#         total+=i["price"]*i["count"]
#     print(f"商品的价格为{total}")
#     if total>=5000 and coupon<=total:
#         total-=coupon
#         print(f"经过优惠后的价格为{total}")
#     else:
#         print("不能优惠")
#     if total>=5000 and points//100<total:
#         total-=points//100
#         print(f"积分折扣后的价格为{total}")
#     else:
#         print("不能优惠")
#     total+=shipping
#     print(f"加上运费后，最后的价格为{total}")
#     return total
# items = [
#     {'name': 'iPhone', 'price': 5000, 'count': 1},  # 第1个商品（字典）
#     {'name': 'iPad',   'price': 3000, 'count': 2}   # 第2个商品（字典）
# ]
# calculate_order_total(items,500,100000,50)
# 简单的运费计算器
# def calculate_shipping(amount,is_vip):
#     total=0
#     if is_vip=="false":
#
#         if amount<99:
#             total+=10
#             print("运费10元")
#         elif amount>=99:
#             total+=0
#             print("免运费")
#     elif is_vip=="true":
#         print("尊贵的vip用户，免运费")
#         total+=0
#     return total
# calculate_shipping(99,"true")
# 定义一个函数，计算订单的总金额
# def goods_total(items,discount,points,shipping):
#     total=0
#     for item in items:
#         total+=item["价格"]*item["数量"]
#     print(f"商品总价为{total}")
#     if total >=5000:
#         total-=discount
#         print(f"优惠后是价格为{total}")
#     else:
#         print(f"未满5000，不能优惠")
#     if total>=5000:
#         a=points//100
#         total-=a
#         print(f"使用积分后，价格为{total}")
#     else:
#         print(f"未满5000，不能使用积分")
#     total+=shipping
#     print(f"该订单总金额为{total}")
# goods=[{"名称":"苹果","数量":300 ,"价格":1 },
#        {"名称":"西瓜","数量":500,"价格":1 },
#         {"名称":"草莓","数量":1000,"价格":1 }
# ]
# goods_total(goods,50,500,77)
# 阶梯式批发折扣
# 单价*数量
# def calculate_wholesale(price,quantity):
#
#     total=price*quantity
#     print(f"商品总价为{total}")
#     if quantity<10:
#         print(f"无折扣")
#     elif quantity<50:
#         total=total*0.9
#         print(f"可享受九折优惠,总价为{total:.2f}")
#     elif quantity<100:
#         total*=0.8
#         print(f"可享受八折折优惠,总价为{total:.2f}")
#     elif quantity>=100:
#         total*=0.7
#         print(f"可享受七折优惠,总价为{total:.2f}")
#     return total
# calculate_wholesale(100,100)
# 购物车满减与叠加优惠
# def checkout(cart,full_reduction,has_member_card):
#     total=0
#     for i in cart:
#         total+=i["数量"]*i["价格"]
#     print(f"商品总价为{total}")
#     if has_member_card:
#         total*=0.95
#         if total>=full_reduction:
#             total-=50
#             if total>=0:
#                 print(f"会员用户的总价为{total}")
#             else:
#                 print("不好意思商品价格不能为0")
#         else:
#             print(f"未达到满减金额")
#     else:
#         if total>=full_reduction:
#             total-=50
#             if total>=0:
#                 print(f"会员用户的总价为{total}")
#             else:
#                 print("不好意思，商品价格不能为0")
#         else:
#             print(f"未达到满减金额")
#     return total
# cart=[{"名称":"苹果","数量":300 ,"价格":1 },
#        {"名称":"西瓜","数量":500,"价格":1 },
#         {"名称":"草莓","数量":1000,"价格":1 }]
# checkout(cart,1000,False)
# 运费匹配  math.ceil()向上取整
# import math
#
#
# def get_shipping_fee(region,weight):
#     shipping=0
#     rules = {
#         "江浙沪": {"base": 5, "extra": 1},  # 首重5元，续重1元/kg
#         "北京": {"base": 10, "extra": 5},  # 首重10元，续重5元/kg
#         "新疆": {"base": 20, "extra": 15}  # 首重20元，续重15元/kg
#     }
#     if region in rules:
#         if weight<=1:
#             shipping=rules[region]["base"]
#             print(f"运费价格为{shipping}")
#         else:
#             a=math.ceil(weight-1)
#             shipping=rules[region]["base"]+a*rules[region]["extra"]
#             print(f"运费价格为{shipping}")
#     else:
#         print("配送不在范围内")
#     return shipping
# get_shipping_fee("北京",2.3)
# 指定类型注解 (冒号后面加空格)
# a: int=675
# b: float=34.56
# c: str="六一"
# d: bool=True
# e: None=None
# print(f"{a},{b},{c},{d},{e}")
# l: list[str|int |float]=["西瓜","哈密瓜","龙虾"]
# # 列表里面的元素是str类型或者int类型,float类型
# s: set[str]={"123876","987432"}# 集合
# d1: dict[str,int]={"字典":5,"圆规":3}
# t: tuple[str,int,int]=("平板",4996,1)
# l.append("草莓")
# l.append(999)
# l.append(5.7)
# print(f"{l},\n{s},\n{d1},\n{t}")
# 计算圆的面积
# 定义类，面向对象 类名的命名规范，开头字母为大写且单词之间无间隔
# eg:VocalEver
# class Car:
#     pass
# #创建对象
# c1=Car()
# c1.name="XS"
# c1.brand="BMW"
# c1.price=5000000
# print(c1.__dict__)
# # 创建对象 冰箱
# class Refrigerator:
#     pass
# r1=Refrigerator()
# r1.brand="WER"
# r1.price=6000
# r1.name="HER"
# r1.color="black"
# print(r1.__dict__)  #  输出r1的所有属性
# 规范的定义类的方法
# class Car:
#     def __init__(self,c_brand,c_name,c_price):
#         self.brand=c_brand
#         self.name=c_name
#         self.price=c_price
# c1=Car("kwx","xs","50000")
# print(c1.__dict__)
# class Refrigerator:
#      def __init__(self,brand,name,price):
#          self.brand=brand
#          self.name=name
#          self.price=price
# r1=Refrigerator("kwd","pro",4999)
# print(r1.__dict__)
# r2=Refrigerator("AS","I300",9000)
# print(r2.__dict__)
# class Car:
#     # 定义属性
#     def __init__(self,brand,color,name,price):
#         self.brand=brand
#         self.color=color
#         self.name=name
#         self.price=price
#     # 定义跑
#     def running(self):
#         print(f"{self.name},{self.brand}正在高速行驶中")
#
#     # 定义发布价
#     def total_cost(self,rate,discount):
#         return self.price*rate+self.price*discount
# # 调用函数
# c1=Car("奔驰","黑色","E300",100000)
# cost=c1.total_cost(0.8,0.1)
# print(f"该车辆的总价为{cost:.1f}")
# c1.running()
# 定义平板
# class Tablet:
#     #  类属性
#     pen=1
#     tax_rate=0.1
#     # self--实例属性
#     def __init__(self,color,name,brand,price):
#         self.color=color
#         self.name=name
#         self.brand=brand
#         self.price=price
#     def function(self):
#         print(f"{self.name},{self.brand}可以下载大量游戏")
#     def total_price(self,discount,shipping):
#         return self.price*discount+shipping
#     def __eq__(self,other):
#         return self.price==other.price and self.name == other.name
#     def __lt__(self,other):
#         return self.price<other.price
#     def __str__(self):
#         return f"{self.name},{self.brand}"
# # 调用函数
# t1=Tablet("白色","荣耀","ipad3",4999)
# t2=Tablet("黑色","荣耀","ipad3",4999)
# # price1=t1.total_price(0.8,0.1)
# # print(f"该商品总价为{price1:.1f}")
# # t1.function()
# print(t1==t2)
# print(t1<t2)
# print(t1)
# #  本来输出的内存地址，加上__str__,变成了字符串存储
# print(t1.pen)
#  教务管理系统的开发（面向对象）
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"{self.name},{self.chinese},{self.math},{self.english}"


# 调用Student,
# s1=Student("李明",56,34,57)
# print(s1.__dict__)
# 对象————————教育管理系统
class Education:
    def __init__(self):
        self.student = []

    # 1,添加学生信息
    def add_student(self):
        name = input("请输入学生姓名")
        for student in self.student:
            if student.name == name:
                print("该学生已存在，请勿重新输入")
        else:
            try:
                chinese = float(input("请输入该生新的语文成绩"))
                math = float(input("请输入该生新的数学成绩"))
                english = float(input("请输入该生新的英语成绩"))
                student = Student(name, chinese, math, english)
                self.student.append(student)
                print("该学生添加成功")
            except ValueError:
                print("输入的成绩有误，请重新输入")

    # 2,修改学生成绩
    def update_student(self):
        name = input("请输入学生姓名")
        for student in self.student:
            if student.name == name:
                try:
                    chinese = float(input("请输入该生新的语文成绩"))
                    math = float(input("请输入该生新的数学成绩"))
                    english = float(input("请输入该生新的英语成绩"))
                    student.chinese = chinese
                    student.math = math
                    student.english = english
                    print("修改成功")
                except ValueError:
                    print("输入错误，请重新输入")
        else:
            print("没有该学生，请重新输入")

    # 3,查询学生成绩
    def qurry_student(self):
        name = input("请输入学生姓名")
        result = [student for student in self.student if student.name == name]
        # 这么写，写不了else,即没有找到怎么办？
        if result:
            print(result[0])
        else:
            print("未找到该生的信息")

    # 4,删除学生信息
    def delete_student(self):
        name = input("请输入要删除的学生姓名")
        for student in self.student:
            if student.name == name:
                return [student for student in self.student if student.name != name]
        print("删除成功")

    # 5,展示全部学生信息
    def show_student(self):
        print("\n>>>>>>全部学生成绩如下")
        for student in self.student:
            print(student)

    def run(self):
        while True:
            print("""
        >>>>>>>>>>>>>欢迎来到教育管理系统<<<<<<<<<<<<<<<<<<<<
        1,添加学生成绩
        2,修改学生成绩
        3,查询学生成绩
        4,删除学生信息
        5,展示学生信息
        """)
            choice = int(input("请输入你的选择"))
            match choice:
                case 1:
                    self.add_student()

                case 2:
                    self.update_student()

                case 3:
                    self.qurry_student()

                case 4:
                    self.update_student()

                case 5:
                    self.show_student()

                case _:
                    print("输入错误请重新输入")


if __name__ == "__main__":
    system = Education()
    system.run()
