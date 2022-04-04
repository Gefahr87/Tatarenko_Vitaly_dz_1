print('Hello, \'Disney\' world')

'''
# int - только целые числа
# float - все возможные дробные числа
'''
# shop_item_str = input('Insert item cost: ')
# shop_item = float(shop_item_str)
# print(type(shop_item), type(shop_item_str))

'''
item_number = 10
total_price = 0
while item_number > 0:
     shop_item = float(input('Insert item cost: '))
     total_price += shop_item
     item_number -= 1
     print(total_price)
'''

item_number = 2
total_price = 0
for i in range(item_number): #range(start, end, step)
     total_price += float(input('Insert item cost: '))
'''
/ - деление, вернёт float с дробной частью
// - вернут float, но только с целой частью
'''


rub_500 = total_price // 500
left_money = total_price % 500 # что осталось после 500

print(rub_500, left_money)
rub_20 = left_money // 20
left_money = left_money % 20
print(rub_20, left_money)