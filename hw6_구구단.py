

def display_multiplication_table(n):
    for i in range(1,10):
        for j in range(n, n+4):
            print(f'{j} x {i} = {j*i}', end='\t')
        print()
    print()
    
display_multiplication_table(2)
display_multiplication_table(6)