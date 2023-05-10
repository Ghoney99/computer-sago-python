# User-defined module Class_StopWatch.py
import time
from tkinter import *

class StopWatch():
    def __init__(self, win):
        self.win = win  #윈도우 매개변수
        win.title("21812055 Timer") #타이틀
        win.geometry("230x90") #윈도우 크기설정
        self.elapsed_time = 0.0 #타이머의 시간
        self.running = False #타이머가 작동하고 있는가

        # 화면에 표시할 Text 객체 생성
        self.timeText = Label(win, text='0.0', font=("Arial 40 bold")) #타이머 숫자 디폴트값은 0.0이고 폰트는 bold체 40사이즈
        self.timeText.pack()

        # 버튼 생성 /매개변수: 윈도우, 너비, 배경색, 텍스트, 커맨드
        self.startBtn = Button(win, width=10, bg="green", text='Start', command=self.start)   #시작버튼 생성
        self.startBtn.pack(side=LEFT)   #버튼을 왼쪽으로 덧붙임

        self.pauseBtn = Button(win, width=10, bg="red", text='Pause', command=self.stop)    #일시정지버튼
        self.pauseBtn.pack(side=LEFT)

        self.resetBtn = Button(win, width=10, bg="yellow", text='Reset', command=self.reset)   #리셋버튼
        self.resetBtn.pack(side=LEFT)

    def runTimer(self):
        if self.running:
            self.elapsed_time += 0.001  #시간은 0.001초씩 더함
            self.timeText.configure(text="{:.3f}".format(self.elapsed_time))
        self.win.after(1, self.runTimer) # 1ms 후에 다시 실행

    def start(self):
        if not self.running:    #타이머가 진행되지않은 상태면 실행
            self.running = True
            self.start_time = time.time()
            self.runTimer()

    def stop(self): #타이머가 진행 상태면 실행
        if self.running:
            self.running = False
            self.elapsed_time += time.time() - self.start_time

    def reset(self):    #타이머를 진행되지 않은 상태로 만들고 시간을 0.0으로 리셋
        self.running = False
        self.elapsed_time = 0.0
        self.timeText.configure(text='0.0')

