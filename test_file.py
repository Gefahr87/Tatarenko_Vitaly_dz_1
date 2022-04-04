# print('Hello, \'Disney\' world')
#
# '''
# int - только целые числа
# float - все возможные дробные числа
# '''
# # shop_item_str = input('Insert item cost: ')
# # shop_item = float(shop_item_str)
# # print(type(shop_item), type(shop_item_str))
#
#
# item_number = 10
# total_price = 0
# while item_number > 0:
#     shop_item = float(input('Insert item cost: '))
#     total_price += shop_item
#     #
#     item_number -= 1
'''
случай с ошраничением на траты (не больше 420 рублей)
'''

left_money = 420
total_price = 0
while total_price <= 420: # цикл по условию
    shop_item = float(input('Insert item cost: '))

    if (left_money - shop_item) > 0:
        print('block 1')
        total_price += shop_item
        left_money = 420 - total_price
        # left_money -= shop_item
    elif (left_money - shop_item) == 0:
        print('block 2')
        total_price += shop_item
        left_money = 420 - total_price
        break
    else:
        print('Oops, no money :(')
        break

    print('You steel have ', left_money)


print(total_price)

"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

