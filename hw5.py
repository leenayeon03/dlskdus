#사용자 함수 정의

def read_single_digit(n):
    if n == 0:
        return "영"
    elif n == 1:
        return "일"
    elif n == 2:
        return "이"
    elif n == 3:
        return "삼"
    elif n == 4:
        return "사"
    elif n == 5:
        return "오"
    elif n == 6:
        return "육"
    elif n == 7:
        return "칠"
    elif n == 8:
        return "팔"
    elif n == 9:
        return "구"
    
def read_number(num):
    n100 = num//100
    n10 = (num%100)//10
    n1 = num%10
    return n100, n10, n1


#주 프로그램부
num = int(input('세 자리 정수 입력 : '))
n100, n10, n1 = read_number(num)
print(f'{read_single_digit(n100)} {read_single_digit(n10)} {read_single_digit(n1)}')