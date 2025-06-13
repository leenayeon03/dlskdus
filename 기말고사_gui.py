
import tkinter as tk
from tkinter import ttk

def buildGUI():
    text_label1 = ttk.Label(win, text='안녕하세요')
    
    text_label2 = ttk.Label(win)
    text_label2.configure(text='반가워요',
                          foreground='white',
                          background='Red',
                          font=('맑은고딕, 20')
    )
    
    text_label1.pack()
    text_label2.pack()
    
win = tk.Tk()
win.title('라벨 위젯 예1')
buildGUI()
win.mainloop()

#위젯의 기본 스타일 이름 반환
import tkinter as tk
from tkinter import ttk

w = ttk.Label(None)
print(w.winfo_class()) #Label 위젯의 기본 스타일 이름 출력


#라벨 위젯의 스타일 설정
def buildGUI():
    s = ttk.Style() #스타일 객체 생성
    s.configure('WR.TLabel', #새 스타일 이름
                foreground='white',
                background='red',
                font=('맑은고딕',20)
                
                ) 
    
    text_label1 = ttk.Label(win, text='안녕하세요', style='WR.TLabel')
    text_label2 = ttk.Label(win)
    text_label2.configure(text='반가워요',style='WR.TLabel')
    
    text_label1.pack()
    text_label2.pack()
    
win = tk.Tk()
buildGUI()
win.mainloop()

#버튼 위젯
import tkinter as tk
from tkinter import ttk

def buildGUI():
    global text_label #이벤트 핸들러에서 접근 위해
    text_label = ttk.Label(win, text='안녕하세요')
    
    input_btn = ttk.Button(win, text='입력', command=input_btn_handler)
    quit_btn = ttk.Button(win, text='종료', command=win.destroy)
    
    text_label.pack()
    input_btn.pack()
    quit_btn.pack()
    
def input_btn_handler(): #버튼 클릭에 대한 이벤트 핸들러 함수
    text_label.configure(text='반가워요')
    
win = tk.Tk()
buildGUI()
win.mainloop()

#엔트리 위젯
import tkinter as tk
from tkinter import ttk

def buildGUI():
    global text_label
    text_label = ttk.Label(win, text='안녕하세요')
    
    global name
    name = tk.StringVar()
    input_entry = ttk.Entry(win, textvariable=name)
    
    input_btn = ttk.Button(win, text='입력', command=input_btn_handler)
    quit_btn = ttk.Button(win, text='종료',command=win.destroy)
    
    text_label.pack()
    input_entry.pack()
    input_btn.pack()
    quit_btn.pack()
    
def input_btn_handler():
    text_label.configure(text='반가워요, ' + name.get())
    name.set('')
    
win = tk.Tk()
buildGUI()
win.mainloop()

#텍스트 위젯
import tkinter as tk
from tkinter import ttk

def buildGUI():
    global text_area
    text_area = tk.Text(win, width=30, height=5, wrap=tk.WORD)
    
    input_btn = ttk.Button(win, text='출력',command=input_btn_handler)
    
    text_area.pack()
    input_btn.pack()
    
def input_btn_handler():
    print(text_area.get(0.0,tk.END))
    text_area.delete(0.0,tk.END)
win = tk.Tk()
buildGUI()
win.mainloop()


#스크롤 텍스트 위젯
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def buildGUI():
    global text_area
    text_area = scrolledtext.ScrolledText(win, width=30, height=5, wrap=tk.WORD)
    text_area.pack()
    
def input_btn_handler():
    print(text_area.get(0.0, tk.END))
    text_area.delete(0.0,tk.END)
    
win = tk.Tk()
buildGUI()
win.mainloop()

#체크 버튼 위젯
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def buildGUI():
    global check
    check = tk.IntVar()
    check_btn = ttk.Checkbutton(win, text='옵션을 선택하세요',variable=check,command=open_dialog_box)
    
    check_btn.pack()
    
def open_dialog_box():
    if check.get() == 1:
        messagebox.showinfo('확인','옵션 선택')
    else:
        messagebox.showinfo('확인','옵션 해제')
        
win = tk.Tk()
buildGUI()
win.mainloop()

#라디오 버튼 (누르는 것마다 색깔 바뀜)
import tkinter as tk
from tkinter import ttk

GENDERS = ['남성','여성','기타']
COLORS = ['red','yellow','purple']

def buildGUI():
    text_label = ttk.Label(win, text='당신의 성별은? ')
    text_label.pack()
    
    global gender
    gender = tk.IntVar() #체크 상태 저장을 위해
    for i in range(3):
        radio_btn = ttk.Radiobutton(win,
                    text = GENDERS[i],
                    value = i
                    variable=gender,
                    command=radio_btn_hadler
        )
        radio_btn.pack()
    gender.set(-1) #라디오 버튼 선택 지우기
    
def radio_btn_hadler():
    choice = gender.get()
    win.configure(background=COLORS[choice])

win = tk.Tk()
win.title('버튼 위젯 예')
buildGUI()
win.mainloop()

#위젯 배치
import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='버튼2')
    btn3 = ttk.Button(win, text='버튼3')
    btn4 = ttk.Button(win, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')
    
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()
    
win = tk.Tk()
win.title('pack 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()

#위젯 배치 (side)
import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='버튼2')
    btn3 = ttk.Button(win, text='버튼3')
    btn4 = ttk.Button(win, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')
    
    btn1.pack(side=tk.BOTTOM)
    btn2.pack(side = tk.LEFT)
    btn3.pack(side = tk.RIGHT)
    btn4.pack()
    btn5.pack(side = tk.TOP)
    
win = tk.Tk()
win.title('pack 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()

#위젯 여백 지정(ipad, pad)
import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='버튼2')
    btn3 = ttk.Button(win, text='버튼3')
    btn4 = ttk.Button(win, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')
    
    btn1.pack()
    btn2.pack(ipadx=10, ipady=10)
    btn3.pack(padx = 10, pady=10)
    btn4.pack(fill=tk.X)
    btn5.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)
    #ipadx : 위젯의 왼쪽과 오른쪽의 안쪽 여백
    #ipady : 위쪽과 아래쪽의 안쪽 여백
    #padx : 위젯의 왼쪽과 오른쪽의 바깥여백
    #pady : 위쪽과 아래쪽의 바깥여백
win = tk.Tk()
win.title('pack 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()

#위젯배치 (grid)
import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='버튼2')
    btn3 = ttk.Button(win, text='버튼3')
    btn4 = ttk.Button(win, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')
    
    btn1.grid(row=0, column = 0, sticky='se')
    #sticky = 정렬방향
    btn2.grid(row=0, column=1)
    btn3.grid(row=1, column=1, sticky='w')
    btn4.grid(row=1, column=2)
    btn5.grid(row=2, column=0)
    
win = tk.Tk()
win.title('pack 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()

#셀 합치기(columnspan, rowspan)
import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='매우 긴~~~ 너비와 높이를 갖는\n버\n튼\n2')
    btn3 = ttk.Button(win, text='버튼3')
    btn4 = ttk.Button(win, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')
    
    btn1.grid(row=0, column = 0, sticky='se')
    btn2.grid(row=0, column=1,columnspan=2)
    btn3.grid(row=1, column=1, sticky='w')
    btn4.grid(row=1, column=2)
    btn5.grid(row=2, column=0)
    
win = tk.Tk()
win.title('pack 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()

#프레임을 이용한 배치
import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='매우 긴~~~ 너비와 높이를 갖는\n버\n튼\n2')
    btn_group = ttk.Frame(win)
    btn3 = ttk.Button(btn_group, text='버튼3')
    btn4 = ttk.Button(btn_group, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')
    
    btn1.grid(row=0, column = 0, sticky='se')
    btn2.grid(row=0, column=1)
    btn3.pack(side=tk.LEFT)
    btn4.pack(side=tk.LEFT)
    btn_group.grid(row=1, column=1, sticky='w')
    btn5.grid(row=2, column=0)
    
win = tk.Tk()
win.title('pack 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()

#엔트리 위젯의 사용
import tkinter as tk
from tkinter import ttk

def buildGUI():
    global text_label
    text_label = ttk.Label(win, text='안녕하세요')
    
    global name
    name = tk.StringVar()
    
def input_btn_handler():
    text_label.configure(text='반가워요, '+name.get())
    name.set() #작은 따옴표 두 개로 빈문자열을 인수로 지정
    
win = tk.Tk()
win.title('버튼 위젯 예')
buildGUI()
win.mainloop()


#객체지향적으로 Gui 구성
import tkinter as tk
from tkinter import ttk

class SayHelloWin:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('버튼 위젯 예')
        self.__buildGUI()
    def __buildGUI(self):
        self.text_label = ttk.Label(self.win, text='안녕하세요')
        
        self.name = tk.StringVar()
        input_entry = ttk.Entry(self.win,
                                textvariable=self.name)
        input_btn = ttk.Button(self.win, text='입력',
                               command=self.__input_btn_handler)
        quit_btn = ttk.Button(self.win, text='종료',
                              command=self.win.destroy)
        
        self.text_label.pack()
        input_entry.pack()
        input_btn.pack()
        quit_btn.pack()
        
    def __input_btn_handler(self):
        self.text_label.configure(
            text='반가워요, '+self.name.get())
        self.name.set('')
hello = SayHelloWin()
hello.win.mainloop()

#좀 더 복잡한 화면 구성
import tkinter as tk
from tkinter import ttk

class SayHelloWin:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('버튼 위젯 예')
        self.__buildGUI()
        
    def __buildGUI(self):
        self.__create_input_frame().pack()
        self.__create_button_frame().pack()
        
    def __create_input_frame(self):
        frame = ttk.Frame(self.win)
        
        self.text_label = ttk.Label(frame, text='안녕하세요')
        
        self.name = tk.StringVar()
        input_entry = ttk.Entry(frame, textvariable=self.name)
        
        self.text_label.grid()
        input_entry.grid(row=0, column=1)
        
        return frame
    
    def __create_button_frame(self):
        frame = ttk.Frame(self.win)
        
        input_btn = ttk.Button(frame, text='입력', command=self.__input_btn_handler)
        quit_btn = ttk.Button(frame, text='종료',command=self.win.destroy)
        
        input_btn.pack(side=tk.LEFT)
        quit_btn.pack(side=tk.LEFT)
        
        return frame
    
    def __input_btn_handler(self):
        self.text_label.configure(
            self.text_label.configure(
                text='반가워요, '+self.name.get()))
        
hello = SayHelloWin()
hello.win.mainloop()


#섭씨 화씨
import tkinter as tk
from tkinter import ttk

class ConvTempWin():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('온도변환기-1단계')
        self.__buildGUI()
        self.win.geometry("270x190")
        
    def __buidGUI(self):
        f_Label = ttk.Label(self.win, text='화씨')
        self.__f = tk.IntVar()
        f_entry = ttk.Entry(self.win, justify=tk.RIGHT, width=11, textvariable=self.__f)
        
        c_Label = ttk.Label(self.win, text='섭씨')
        self.__c = tk.DoubleBar()
        c_entry = ttk.Entry(self.win, justify=tk.RIGHT, width=11, textvariable=self.__c)
        
        ftoc_btm = ttk.Button(self.win, text='화씨->섭씨', command=self.__ftoc_handler)
        ctof_btm = ttk.Button(self.win, text='섭씨->화씨', command=self.__ctof_handler)
        reset_btm = ttk.Button(self.win, text='초기화', command=self.__reset_handler)
        quit_btm = ttk.Button(self.win, text='종료', command=self.win.destroy)
        
        f_Label.pack()
        f_entry.pack()
        c_Label.pack()
        c_entry.pack()
        
        ftoc_btm.pack()
        ctof_btm.pack()
        reset_btm.pack()
        quit_btm.pack()
        
        
        def __ftoc_handler(self):
            f = self.__f.get()
            c = (f-23)/1.8
            self.__c.set(f'{c:.2f}')
            
        def __ctof_handler(self):
            c = self.__c.get()
            f = (f*1.8) + 32
            self.__f.set(f'{f:.0f}')
            
        def __reset_handler(self):
            self.__f.set('')
            self.__c.set('')
            
        def start(self):
            self.win.mainloop()
            
tCOnveter = ConvTempWin()
tCOnveter.start()

#그리드 사용한 온도변환
import tkinter as tk
from tkinter import ttk

class ConvTempWin():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('온도변환기-2단계')
        self.__buildGUI()
        
    def __buildGUI(self):
        # 화씨
        f_Label = ttk.Label(self.win, text='화씨')
        self.__f = tk.IntVar()
        f_entry = ttk.Entry(self.win, justify=tk.RIGHT, width=11, textvariable=self.__f)
        
        # 섭씨
        c_Label = ttk.Label(self.win, text='섭씨')
        self.__c = tk.DoubleVar()
        c_entry = ttk.Entry(self.win, justify=tk.RIGHT, width=11, textvariable=self.__c)
        
        # 버튼
        ftoc_btn = ttk.Button(self.win, text='화씨->섭씨', command=self.__ftoc_handler)
        ctof_btn = ttk.Button(self.win, text='섭씨->화씨', command=self.__ctof_handler)
        reset_btn = ttk.Button(self.win, text='초기화', command=self.__reset_handler)
        quit_btn = ttk.Button(self.win, text='종료', command=self.win.destroy)
        
        # 배치
        f_Label.grid(row=0, column=0)
        f_entry.grid(row=0, column=1)
        c_Label.grid(row=0, column=2)
        c_entry.grid(row=0, column=3)
        ftoc_btn.grid(row=1, column=0)
        ctof_btn.grid(row=1, column=1)
        reset_btn.grid(row=1, column=2)
        quit_btn.grid(row=1, column=3)
        
    def __ftoc_handler(self):
        f = self.__f.get()
        c = (f - 32) / 1.8
        self.__c.set(f'{c:.2f}')
        
    def __ctof_handler(self):
        c = self.__c.get()
        f = (c * 1.8) + 32
        self.__f.set(f'{f:.0f}')
        
    def __reset_handler(self):
        self.__f.set(0)
        self.__c.set(0.0)
        
    def start(self):
        self.win.mainloop()
        
tempConverter = ConvTempWin()
tempConverter.start()



#프레임 위젯 사용한 온도변환
import tkinter as tk
from tkinter import ttk

class ConvTempWin():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('온도변환기-3단계')
        self.__buildGUI()
        
    def __buildGUI(self):
        self.__create_input_frame().pack()
        self.__create_button_frame().pack()
        
    def __create_input_frame(self):
        frame = ttk.Frame(self.win)
        f_Label = ttk.Label(self.win, text='화씨')
        self.__f = tk.IntVar()
        f_entry = ttk.Entry(frame, justify=tk.RIGHT, width=11, textvariable=self.__f)
        
        c_Label = ttk.Label(frame, text='섭씨')
        self.__c = tk.DoubleVar()
        c_entry = ttk.Entry(frame, justify=tk.RIGHT, width=11, textvariable=self.__c)
        

        f_Label.pack(side=tk.LEFT)
        f_entry.pack(side=tk.LEFT)
        c_Label.pack(side=tk.LEFT)
        c_entry.pack(side=tk.LEFT)
        
        return frame
        

        
    def __create_button_frame(self):
        frame=ttk.Frame(self.win)
        ftoc_btm = ttk.Button(frame, text='화씨->섭씨', command=self.__ftoc_handler)
        ctof_btm = ttk.Button(frame, text='섭씨->화씨', command=self.__ctof_handler)
        reset_btm = ttk.Button(frame, text='초기화', command=self.__reset_handler)
        quit_btm = ttk.Button(frame, text='종료', command=self.win.destroy)
        
        ftoc_btm.pack(side=tk.LEFT)
        ctof_btm.pack(side=tk.LEFT)
        reset_btm.pack(side=tk.LEFT)
        quit_btm.pack(side=tk.LEFT)
        
        return frame
    
    def __ftoc_handler(self):
        f = self.__f.get()
        c = (f-23)/1.8
        self.__c.set(f'{c:.2f}')
            
    def __ctof_handler(self):
        c = self.__c.get()
        f = (f*1.8) + 32
        self.__f.set(f'{f:.0f}')
            
    def __reset_handler(self):
        self.__f.set('')
        self.__c.set('')
            
    def start(self):
        self.win.mainloop()
            
tCOnveter = ConvTempWin()
tCOnveter.start()



#사용자 정보 입력 처리
import tkinter as tk
from tkinter import ttk

class MemberReg():
    hobby_list = ['영화시청','음악감상','사진찍기','운동']
    
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('회원가입')
        self.__buildGUI()
        
    def buildGUI(self):
        self.__create_name_input_frame().grid(row=0, column=0,sticky='w')
        self.__create_grade_input_frame().grid(row=1, column=0, sticky='w')
        self.__create_hobby_input_frame().grid(row=2, column=0, sticky='w')
        self.__create_button_frame().grid(row=3, column=0, sticky='e')
        
    def __create_name_input_frame(self):
        frame = ttk.Frame(self.win)
        
        self.text_label = ttk.Label(frame, text='이름 : ')
        self.name = tk.StringVar()
        input_entry = ttk.Entry(frame, textvariable=self.name)
        
        self.text_label.grid(row=0, column=0)
        input_entry.grid(row=0, column=1)
        
        return frame
    def __create_grade_input_frame(self):
        frame = ttk.Frame(self.win)
        self.text_label = ttk.Label(frame, text='학년: ')
        sub_frame = ttk.Frame(frame) #학년 선택 버튼을 담을 하위 프레임 생성
        self.grade = tk.IntVar()
        for i in range(1,5):
            grade_btn = ttk.Radiobutton(sub_frame, text=f'{i}학년', value=i, variable=self.grade) #radio:하나만 선택
            grade_btn.pack(side=tk.LEFT)
        sub_frame.grid(row=0, column=1)
        
        return frame
    
    def __create_hobby_input_frame(self):
        frame = ttk.Frame(self.win)
        
        self.text_label = ttk.Label(frame, text='취미: ')
        self.text_label.grid(row=0, column=0)
        sub_frame = ttk.Frame(frame)
        self.hobby = []
        
        for i in range(4):
            self.hobby.append(tk.IntVar())
            hobby_btn = ttk.Checkbutton(sub_frame, text=self.hobby_list[i],
                                        variable=self.hobby[i])
            hobby_btn.pack(side=tk.LEFT)
        sub_frame.grid(row=0, column=1)
        
        return frame
            
    def __create_button_frame(self):
        frame = ttk.Frame(self.win)
        input_btn = ttk.Button(frame, text='입력', command=self.__input_btn_clicked)
        quit_btn = ttk.Button(frame, text='종료', command=self.win.destory)
        
        input_btn.pack(side=tk.LEFT)
        quit_btn.pack(side=tk.LEFT)
        
        return frame
    
    def __input_btn_clicked(self):
        print(self.name.get())
        print(self.grade.get())
        
        for i in range(4):
            if self.hobby[i].get() == True:
                print(self.hobby_list[i])
    
member = MemberReg()
member.win.mainloop()

#단어장
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

class Word:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('단어장')
        self.win.geometry('400x100')
        self.buildGUI()
        self.words = self.loadData()
        
    def buildGUI(self):
        l_word= ttk.Label(self.win, text='단어: ')
        self.word = tk.StringVar()
        e_word= ttk.Entry(self.win, textvariable=self.word, width=15) #textvariable : self.word와 연결하는 입력창을 만듦
        
        l_mean = ttk.Label(self.win, text='뜻: ')
        self.mean = tk.StringVar()
        e_mean = ttk.Entry(self.win, textvariable=self.mean, width=35)
        
        #
        b_search = ttk.Button(self.win, text='검색', width=5, command=self.search)
        b_add = ttk.Button(self.win, text='추가', width=5, command=self.add)
        b_reset = ttk.Button(self.win, text='초기화', width=5, command=self.reset)
        b_exit = ttk.Button(self.win, text='종료', width=5 ,command=self.end)
        
        
        l_word.grid(row=0, column=0, sticky='e', padx=10)
        e_word.grid(row=0, column=1, sticky='w')
        
        b_search.grid(row=0, column=2, ipadx=10, ipady=5, sticky='w')
        b_add.grid(row=0, column=3, ipadx=10, ipady=5, sticky='w')
        
        l_mean.grid(row=2, column=0, sticky='e',padx=10)
        e_mean.grid(row=2, column=1, columnspan=3, sticky='w')
        
        b_reset.grid(row=3, column=0, ipadx=10, ipady=5, padx=10, sticky='w')
        b_exit.grid(row=3, column=1, ipadx=10, ipady=5, sticky='w')
        
    def loadData(self):
        words ={}
        if not os.path.exists('words.txt'):
            return words
        fp = open('words.txt','r',encoding='utf-8')
        
        for line in fp:
            word = line.split(":")
            
            for i in range(0, len(word)):
                word[i] = word[i].strip()
                
            key = word[0]
            value = word[1]
            words[key] = value
            
        fp.close()
        
        return words
    
    def add(self):
        w = self.word.get()
        m = self.mean.get()
        
        self.words[w] = m
        
        messagebox.showinfo('추가 확인', '단어 '+w+'를 추가했습니다')                
        
        self.word.set('')
        self.mean.set('')
                
    def search(self):
        w = self.word.get()
        
        if w not in self.words:
            messagebox.showinfo('검색오류',w+'란 단어는 없습니다!')
            self.reset()
            return
        
        m = self.words[w]
        self.mean.set(m)
        
    def reset(self):
        self.word.set('')
        self.mean.set('')
        
    def end(self):
        fp = open('words.txt','w',encoding = 'utf-8')
        
        for w in self.words.keys():
            m = self.words[w]
            fp.write(w+':'+m+'\n')
            
        fp.close()
        self.win.destroy()
        
    def searchHandler(event):
        search()
    def resetHandler(event):
        reset()
        
wm = Word()
wm.win.mainloop()