# # items 是一个列表 []
# items = [
#     {'name': 'iPhone', 'price': 5000, 'count': 1},  # 第1个商品（字典）
#     {'name': 'iPad',   'price': 3000, 'count': 2}   # 第2个商品（字典）
# ]
# def calculate_order_total(items,coupon,points,shipping):
#     total=0
#     for i in items:
#         total += i["price"]*i["count"]
#     print(f"商品的初始总价为{total}")
#     if coupon > total:
#         print("优惠金额不可超过总价")
#     else:
#         if total >= 5000:
#             print("优惠劵满足条件，可以使用")
#             total = total - coupon
#             print(f"用了优惠劵，现在的价格为{total}")
#         else:
#             print("商品金额满5000才能使用优惠劵")
#     if total > 5000:
#         print("可以使用")
#         if points // 100 != 0:
#             b = points / 100
#             total = total - b
#             print(f"用了积分折扣后，价格为{total}")
#         else:
#             print("抱歉，积分只能整百抵扣")
#     else:
#         print("不可使用")
#
#     total = total + shipping
#     return total
#
# print(calculate_order_total(items,50,506,164))




















