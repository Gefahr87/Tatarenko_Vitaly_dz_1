'''
случай с ограниченим на трату (не больше 420 рублей)
'''

left_money = 420
total_price = 0

while total_price <= 420: #цикл по условию (пока условие: делай то-то
    shop_item = float(input('Insert item cost: ')) #строку к флоат
    if (left_money - shop_item) > 0:
        #если условие выполняется
        # print('Block 1')
        # print(total_price, left_money)
        total_price += shop_item
        left_money = 420 - total_price
        #left_money -= shop_item
        # print(total_price, left_money)
    elif (left_money - shop_item) == 0:
        # сделать без elif
        # если условие иначально не выполнилось, но выполнилось это
        # print('Block 2')
        # print(total_price, left_money)
        total_price += shop_item
        left_money = 420 - total_price
        break
        # print(total_price, left_money)
    else:
        print('Oops, no money :(')
        break

    print('You still have: ', left_money)
    #total_price += float(input('Insert item cost: '))

print(total_price)

"""
    if (left_money - shop_item) > 0:
        #если условие выполняется

        total_price += shop_item
        left_money = 420 - total_price
    
    else:
        if (left_money - shop_item) == 0:
            total_price += shop_item
            left_money = 420 - total_price
            break
        else:
            print('Oops, no money :(')
            break
"""