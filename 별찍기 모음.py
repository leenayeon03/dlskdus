n = int(input('별 찍는 개수: '))

#오른쪽으로 직각삼각형
for i in range(1,n+1):
    for j in range(i):
        print("*", end = '')
    print()
    
#왼쪽 직각삼각형
for i in range(1,n+1):
    print(" "*(n-i) + "*"*i)
    

#왼쪽 위 직각삼각형
for i in range(n,0,-1):
    print("*"*i)
    
#오른쪽 위 직각삼각형
for i in range(1,n+1):
    print(' '*(i-1)+"*"*(n+1-i))
    

#두 개 합치면 다이아몬드
for i in range(1,n+1):
    print(' '*(n-i)+"*"*(i*2-1))
    
    
for i in range(n,0,-1):
    print(' '*(n-i) + '*'*(2*i-1))
    

#리본모양
for i in range(1,n+1):
    print("*" * i + " " * 2*(n-i) + "*" * i)
for j in range(1,n):
    print("*"* (n-j) + " " * 2*j + "*" * (n-j))
    
    

#모래시계
for i in range(n,0,-1):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(2,n+1):
    print(' '*(n-i)+"*"*(i*2-1))
    

#3*3 이상한 모양
def recur(n):
    if n == 1:
        return ['*']
    star = recur(n//3)

    stars = []
    for i in star:
        stars.append(i*3)
    for j in star:
        stars.append(j+' '*(n//3)+j)
    for k in star:
        stars.append(k*3)

    return stars


N = int(input())
print('\n'.join(recur(N)))

#삼각형 이상 모양
import sys
from collections import deque

N=int(sys.stdin.readline().rstrip())
lst=[[0 for i in range(N-1-j)] for j in range(N)]

def pyramid(size,startr,endr): #위에서부터 채워나가기 startr=시작줄 endr=끝줄
    half=size//2
    if size==3:
        lst[startr].append(1)
        lst[startr+1].append(1)
        lst[startr+1].append(0)
        lst[startr+1].append(1)
        for _ in range(5):
            lst[startr+2].append(1)
        return
        
    pyramid(size//2,startr,startr+half)
    pyramid(size//2,startr+half,endr)
    for i in range(startr+half,endr):
        for _ in range(2*(endr-1-i)+1):
            lst[i].append(0)
    pyramid(size//2,startr+half,endr)

pyramid(N,0,N)

for i in range(N):
    for j in range(N-1-i):
        lst[i].append(0)
            

for i in range(N):
    for j in lst[i]:
        if j==0:
            print(' ',end='')
        if j==1:
            print('*',end='')
    print()


#왼쪽 삼각형
for i in range(1, n+1):
    print(' '*(n-i) + '*'*i)
for i in range(1, n):
    print(' '*(i) + '*'*(n-i))
    
    


#오른쪽 삼각형
for i in range(1,n+1):
    print('*'*i)
    
for j in range(n-1, 0, -1):
        print('*'*j)


#속이 빈 삼각형
print(' '*(n-1) + '*')
for i in range(n-1):
    print(' '*(n-2-i) + '*' + ' '*(2*i+1) + '*')
    

#밑에가 n 길이와 동일한 삼각형
for i in range(1,n+1):
     print(" " * (n-i) + "* " * (i-1) + "*")
     
    
#속이 텅 빈 삼각형
for i in range(1, n+1):
    if(i==1 or i==n):
        print(" " * (n-i) + "*" * (2*i-1))
    else:
        print(" " * (n-i) + "*" + " " * (2*(i-1)-1) + "*")
        
    
#속이 텅 빈 삼각형으로 만드는 피라미드
n = int(input())
row = 2 ** n - 1
col = 2 * row - 1
canvas = [[' '] * col for i in range(row)]

# 기준은 맨 왼쪽 위를 0,0 으로 잡고 호출
def draw(x, y, n) :
    row = 2 ** n - 1    # 현재 그릴 삼각형의 행 갯수
    col = 2 * row - 1   # 현재 그릴 삼각형의 열 갯수

    if n == 1 :
        canvas[x][y] = '*'
        return;

    if n % 2 : # 홀수일 경우
        # 이번 삼각형 그리기
        # 각 줄마다 양 끝점 두개 채우기
        for i in range(row-1,-1,-1) :
            canvas[x + row - i - 1][y + i] = '*'
            canvas[x + row - i - 1][y + col - 1 - i] = '*'
            # 맨 아랫줄 채우기
            if i == 0 :
                for j in range(1, col-1) :
                    canvas[x + row - 1][y + j] = '*'
        # 다음 삼각형 호출
        draw(x + 2 ** (n-1) - 1, y + 2 ** (n-1), n - 1)

    else : # 짝수일 경우 (역삼각형)
        # 이번 삼각형 그리기
        # 양 끝점들 채우기
        for i in range(row) :
            canvas[x + i][y + i] = '*'
            canvas[x + i][y + col - 1 - i] = '*'
            # 맨 윗줄 채우기
            if i == 0 :
                for j in range(1, col-1) :
                    canvas[x][y + j] = '*'
        # 다음 그릴 삼각형 호출
        draw(x + 1, y + 2 ** (n-1), n - 1)

draw(0, 0, n)
for line in canvas :
    print(''.join(line).rstrip())
    

#회전 회전

for i in range(n-1):
    print("*" * i +"*"*(1+4*(n-i-1))+"*"*i)
    print("* "*(i+1)+" "*(1+4*(n-i-2))+" *"*(i+1))
print("* "*(2*n-1))
for i in range(n-1):
    print("* "*(n-i-1)+" "*(1+4*i)+" *"*(n-i-1))
    print("* "*(n-i-2)+"*"*(1+4*(i+1))+"*"*(n-i-2))
    

#살랑살랑

if n == 1:
    print('*')
    
else:
    for i in range(n):
        if i % 2 == 0:
            a = print('* ' * n)
        else:
            b = print(' *' * n)
            

#살랑살랑2
for _ in range(n):
    print('* '* (n - n//2))
    print(' *'* (n//2))
    
#골뱅이
def expand_space(star_output: list) -> list:
    """주어진 규칙에 맞게 2차원 리스트를 확장합니다."""
    # 가로축의 공간을 확장합니다.
    for x in range(len(star_output)):
        star_output[x].insert(0, " ")
        star_output[x].insert(0, "*")
        star_output[x].append(" ")
        star_output[x].append("*")
    # 세로축의 공간을 확장합니다.
    star_output.insert(0, ["*"] + [" "] * (len(star_output[0]) - 1))
    star_output.insert(0, ["*"] * len(star_output[0]))
    star_output.append(["*"] + [" "] * (len(star_output[0]) - 2) + ["*"])
    star_output.append(["*"] * len(star_output[0]))
    return star_output


def print_star(x: int) -> list:
    """규칙에 맞추어 x에 해당하는 2중 리스트를 리턴합니다."""
    # 2-1. N이 1 또는 2일때는 정해진 포맷의 별을 리턴합니다.
    if x == 1:
        return [["*"]]
    elif x == 2:
        return [
            ["*", "*", "*", "*", "*"],
            ["*", " ", " ", " ", " "],
            ["*", " ", "*", "*", "*"],
            ["*", " ", "*", " ", "*"],
            ["*", " ", "*", " ", "*"],
            ["*", " ", " ", " ", "*"],
            ["*", "*", "*", "*", "*"],
        ]
    # 2-2. N >= 3일 경우, print_star를 재귀적으로 호출합니다.
    # print_star(N - 1)을 호출하여 N - 1일때의 출력을 호출합니다.
    prev_star_output: list = print_star(x - 1)
    # N - 1일 때의 출력에 위아래 2, 양 옆 2만큼 공간 확장
    prev_star_output = expand_space(prev_star_output)
    prev_star_output[2][-2] = "*"
    return prev_star_output


def main():
    # 1. 입력으로 1 <= N <=의 값을 입력받는다.
    N = int(input())
    # 2. 해당 N에 맞는 별이 담긴 리스트를 변수에 저장한다.
    star_list = print_star(N)
    # 2중 리스트에 담겨있는 별을 출력한다.
    for line in map("".join, star_list):
        print(line.rstrip())


if __name__ == "__main__":
    main()



#텅빈 엑스
for i in range(1, n + 1):
    if i == 1 or i == 2 * n:
        print("*" * n + " " * (2 * (n - 1) - 1) + "*" * n)
    elif i != n:
        print(" " * (i - 1) + "*" + " " * (n - 2) + "*" + " " * (2 * (n - i) - 1) + "*" + " " * (n - 2) + "*")
    else:
        print(" " * (i - 1) + "*" + " " * (n - 2) + "*" + " " * (2 * (n - i) - 1) + " " * (n - 2) + "*")

for i in range(n, 0, -1):
    if i == 1 or i == 2 * n:
        print("*" * n + " " * (2 * (n - 1) - 1) + "*" * n)
    elif i != n:
        print(" " * (i - 1) + "*" + " " * (n - 2) + "*" + " " * (2 * (n - i) - 1) + "*" + " " * (n - 2) + "*")