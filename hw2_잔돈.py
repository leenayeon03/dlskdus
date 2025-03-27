def exchange(amount): 
    print('잔돈:', amount, '원')
    
    n500 = amount // 500
    amount %= 500
    
    n100 = amount // 100
    amount %= 100
    
    n50 = amount // 50
    amount %= 50
    
    n10 = amount // 10
    
    print('500원의 동전의 개수:', n500, '\n100원의 동전의 개수:', n100, '\n50원의 동전의 개수:', n50, '\n10원의 동전의 개수:', n10)

amount = int(input('동전으로 교환하고자 하는 금액은? '))
exchange(amount)