def get_fixed_price(rate, discount_price):
    price = discount_price/(1-rate/100)
    return (price)


discount = int(input('할인율은?'))
A = int(input('A상품의 할인된 가격은?'))
B = int(input('B상품의 할인된 가격은?'))

A_price = int(get_fixed_price(discount, A))
B_price = int(get_fixed_price(discount, B))

print('A상품의 정가는',A_price,'원')
print('B상품의 정가는',B_price,'원')
