# HW 9.2 - My simple stopwatch with class StopWatch
import time
from tkinter import *
from Class_StopWatch import *
if __name__ == '__main__':
    win = Tk()
    stop_watch = StopWatch(win)
    stop_watch.runTimer()
    win.mainloop()