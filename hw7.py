shopping_bag = []
amount = {}

print('[구입]')

while True :
    item = input('상품명? ')
    if item == '':
        break
    amount_item = int(input('수량은? '))
    amount[item] = amount.get(item, 0) + amount_item
    
    shopping_bag.append(item)
    
    print(f'장바구니에 {item} {amount_item}개가 담겼습니다')
    

    
print(f'\n >>> 장바구니 보기: {shopping_bag}')


#검색
print('\n[검색]')

search = input('장바구니에서 확인하고자 하는 상품은?')

if search in amount:
    print(f'{search}은(는) {amount[search]}개 들어있습니다')
else:
    print(f'{search}은(는) 장바구니에 없습니다')