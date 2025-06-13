#점수를 입력 받아, 점수와 평균 출력
scores = []
print('점수 입력')
for i in range (3):
    n = int(input(f'#{i+1}?'))
    scores.append(n)
print('[점수 출력]')
print(f'입력 점수 : {scores[0]} {scores[1]} {scores[2]}')
avg = (scores[0] + scores[1] + scores[2]) / len(scores)
print(f'평균 : {avg:.1f}')

#특정 점수를 받은 학생의 번호 확인 기능
scores = []
print('점수 입력')
for i in range (3):
    n = int(input(f'#{i+1}?'))
    scores.append(n)
print('[점수 출력]')
print(f'입력 점수 : {scores[0]} {scores[1]} {scores[2]}')
avg = (scores[0] + scores[1] + scores[2]) / len(scores)
print(f'평균 : {avg:.1f}')
print('[검색]')
find = int(input('찾고자 하는 점수는?'))
if find in scores:
    num = scores.index(find)
    print(f'{find}점은 {num+1}번 학생의 점수입니다')
else:
    print(f'{find}점을 받은 학생은 없습니다')
    
#장바구니
shopping_bag = []
while True:
    item = input('상품명?')
    if item == '':
        break
    else:
        shopping_bag.append(item)
        print(f'장바구니에 {item}가(이) 담겼습니다.')
        
print('상품명?')
print(f'>>> 장바구니 보기 : {shopping_bag}')

#장바구니에 수량 저장/출력
shopping_bag = []
amount = {}
while True:
    item = input('상품명?')
    if item == '':
        break
    else:
        amount_item = int(input('수량은? '))
        amount[item] = amount.get(item,0) + amount_item
        shopping_bag.append(item)
        print(f'장바구니에 {item}가(이) {amount_item}개가 담겼습니다.')
        
print('상품명?')
print(f'>>> 장바구니 보기 : {amount}')

print('[검색]')
search = input('장바구니에서 확인하고자 하는 상품은? ')
if search in amount:
    print(f'{search}은(는) {amount[search]}개 담겨있습니다')
else:
    print(f'{search}는 장바구니에 없습니다')
    
    
#가장 큰 수 찾기
def find_max():
    l = []
    for i in range(5):
        n = int(input('정수 입력: '))
        l.append(n)
    return max(l)

print(f'가장 큰 정수는 {find_max()}입니다')

#학생 수도 유연하게, 점수 평균
def input_scores():
    scores = []
    i = 1
    while True:
        n = int(input(f'#{i}'))
        if n < 0 :
            break
        else:
            scores.append(n)
            i+=1
    return scores
            
def get_average(scores):
    return sum(scores)/len(scores)

def show_scores(list):
    for n in list:
        print(n,end=' ')
    print()

print('[점수 입력]')
scores = input_scores()

print('[점수 출력]')
print('개인점수:',end=' ')
show_scores(scores)

avg = get_average(scores)
print(f'평균:{avg}')


#특정 점수를 받은 학생의 번호 확인
def search(lst,n):
    if n not in lst:
        return None
    return lst.index(n)
    
print('[검색]')
find_score = int(input('찾고자 하는 점수는?'))
if find_score in scores:
    idx = scores.index(find_score)
    print(f'{find_score}점은 {idx+1}번 학생의 점수입니다.')
    
else:
    print(f'{find_score}점을 받은 학생은 없습니다.')
    

#장바구니에 수량 저장/출력
# 상품 구입 함수
def buy(shopping_bag):
    print('[구입]')
    item = input('상품명? ')
    if item == '':
        return False
    amount = int(input('수량은? '))
    shopping_bag[item] = shopping_bag.get(item, 0) + amount
    print(f'장바구니에 {item} {amount}개가 담겼습니다.')
    return True

# 장바구니 전체 출력 함수
def show(shopping_bag):
    print('\n[장바구니 출력]')
    for item, amount in shopping_bag.items():
        print(f'{item} {amount}괒')

# 상품 검색 함수
def find(shopping_bag):
    print('\n[검색]')
    search = input('장바구니에서 확인하고자 하는 상품은? ')
    if search not in shopping_bag:
        print(f'장바구니에 {search}은(는) 없습니다.')
    else:
        print(f'{search}은(는) {shopping_bag[search]}개 담겨있습니다')

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)

#좌표점을 객체로 표현
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def show(self):
        print(f'({self.__x},{self.__y})')
    def set(self,x,y):
        self.__x = x
        self.__y = y
    def get(self):
        return (self.__x, self.__y)
    
def test():
    p1 = Point()
    p2 = Point(2,3)
    p1.show()
    
    p1.set(10,20); p1.show()
    p2.show()
    
    x,y = p2.get()
    print(f'x={x}, y={y}')
if __name__=='__main__':
    test()
    
#time 클래스
class Time:
    def __init__(self, hour=0, minute= 0):
        self.__hour = hour
        self.__minute = minute
        
    def display(self):
        print(f'{self.__hour:02d}:{self.__minute:02d}')
    def add(self,time):
        h = self.__hour + time.__hour
        m = self.__minute + time.__minute
        if m >= 60:
            h+=1
            m -= 60
        return Time(h,m)
    @staticmethod
    def is_valid(hour, minute):
        if 0 <= hour <= 23 and 0 <= minute <= 59:
            return True
        else:
            return False

def main():
    t1 = Time(9)
    t2 = Time(9,30)
    
    t1.display()
    t2.display()
    
    later = t1.add(Time(1,15))
    later.display()
    
    if Time.is_valid(25,0):
        print('유효한 시각')
    else:
        print('유효하지 않은 시각')
if __name__ == '__main__':
    main()
    
    
#직사각형 둘레, 넓이
class Point:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.lt = Point(x1,y1)
        self.rb = Point(x2,y2)
    
    def show(self):
        print(f'현재 좌측 상단 꼭짓점 : ({self.lt.x} {self.lt.y})')
        print(f'현재 우측 하단 꼭짓점 : ({self.rb.x} {self.rb.y})')
        
    def getWidth(self):
        return (self.rb.x - self.lt.x)
    
    def getHeight(self):
        return (self.rb.y - self.lt.y)
    
    def getArea(self):
        return (self.getWidth() * self.getHeight())
    
    def getPerimeter(self):
        return 2*(self.getWidth() + self.getHeight())
    
r1 = Rectangle(5,5,20,10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'넓이는 {a}, 둘레는 {p}')


#행번호와 내용 출력
def show_file(filename):
    with open(filename, mode='r', encoding='utf8') as file:
        i = 1
        while True:
            line = file.readline()
            
            if line == '':
                break
            print(f'{i}: {line.strip()}')
            i +=1
            
fn = input('파일명: ')
show_file(fn)

#장바구니 프로그램에 save/load 기능 추가
import os

filename = 'shoppingbag.txt'

def buy(sb):
    print('[구입]')
    item = input('상품명? ')
    
    if item =='':
        return False
    
    sb.append(item)
    print(f'장바구니에 {item}가(이) 담겼습니다\n')
    return True

def show(sb):
    print(sb)
    
def save_data(sb,filepath):
    with open(filepath, 'w', encoding='utf8') as file:
        for item in sb:
            file.write(f'{item}\n')
            
def load_data(filepath):
    lines=[]
    with open(filepath, 'r', encoding='utf8') as file:
        for line in file:
            lines.append(line.strip('\n'))
    return lines

if os.path.exists(filename):
    print('[파일 읽기]')
    shopping_bag = load_data(filename)
    show(shopping_bag)
    
else:
    shopping_bag = []
    
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)

save_data(shopping_bag, filename)

#프로그램이 종료된 마지막 시각을 저장
class Time:
    def __init__ (self, hour=0, minute=0):
        self.__hour = hour
        self.__minute = minute
    def display(self):
        return f'{self.__hour:02d}:{self.__minute:02d}'
import os
import pickle
from datetime import datetime

filename = 'last.dat'

def get_current_time():
    now = datetime.now()
    return Time(now.hour, now.minute)

def save_time(time):
    with open(filename, 'wb') as file:
        pickle.dump(time, file)
    
def load_time():
    with open(filename, 'rb') as file:
        t = pickle.load(file)
    return t

if os.path.exists(filename):
    t = load_time()
    print(f'안녕하세요. 마지막으로 {t.display()}에 실행되었습니다')
else:
    print('안녕하세요. 처음 실행되었습니다')
    
t = get_current_time()
print(f'지금은 {t.display()}입니다.')
save_time(t)


#학생 정보 프로그램에 저장/로드 기능 추가
import pickle
import os

def input_scores():
    scores = []
    i = 1
    while True:
        score = int(input(f"#{i}? "))
        if score < 0:
            break
        scores.append(score)
        i += 1
    return scores

def get_average(scores):
    return sum(scores) / len(scores)

def show_scores(scores):
    print("개인점수:", ' '.join(map(str, scores)))
    print(f"평균: {get_average(scores):.1f}")

def save_scores(scores, filename="score.bin"):
    with open(filename, "wb") as f:
        pickle.dump(scores, f)

def load_scores(filename="score.bin"):
    with open(filename, "rb") as f:
        return pickle.load(f)

def main():
    filename = "score.bin"

    if os.path.exists(filename):
        # 파일에서 읽기
        scores = load_scores(filename)
    else:
        # 사용자 입력
        scores = input_scores()
        save_scores(scores, filename)

    show_scores(scores)

main()

