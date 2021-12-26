from tkinter import *
from interface.repeatedTimer import RepeatedTimer
from interface.tetrisPerformer import TetrisPerformer
from random import randint
from random import seed
import time

class Interface():
    def __init__(self):
        self.root = Tk()
        seed(int(time.time() * 10000))
        self.time = 0.5
        self.score = 0
        self.timer = RepeatedTimer(self.time, self.__down, None)
        initalRandom = randint(0, 6)
        nextRandom = randint(0, 6)
        self.performer = TetrisPerformer(initialRandom=initalRandom, nextRandom=nextRandom)
        self.colors = dict({"empty": "white", "iType": "cyan", "jType": "blue", "lType": "orange", "oType": "yellow", "sType": "green", "zType": "red", "tType": "magenta"}) 
        self.colorsPieze = dict({0: "cyan", 1: "blue", 2: "orange", 3: "yellow", 4: "green", 5: "red", 6: "magenta"})
        self.piezePosition = dict({
            0: [(1,21), (2,21), (3,21), (4,21)], 
            1: [(1,21), (2,21), (2,22), (2,23)], 
            2: [(1,23), (2,21), (2,22), (2,23)],
            3: [(1,21), (1,22), (2,21), (2,22)], 
            4: [(1,22), (1,23), (2,21), (2,22)], 
            5: [(1,21), (1,22), (2,22), (2,23)], 
            6: [(1,22), (2,21), (2,22), (2,23)]}) 
        self.holdPosition = dict({
            0: [(12,21), (13,21), (14,21), (15,21)], 
            1: [(12,21), (13,21), (13,22), (13,23)], 
            2: [(12,23), (13,21), (13,22), (13,23)],
            3: [(12,21), (12,22), (13,21), (13,22)], 
            4: [(12,22), (12,23), (13,21), (13,22)], 
            5: [(12,21), (12,22), (13,22), (13,23)], 
            6: [(12,22), (13,21), (13,22), (13,23)]}) 
        self.__initWindow(nextRandom=nextRandom)
        self.root.mainloop()

    def __initWindow(self, nextRandom):
        self.root.geometry('600x720')
        self.root.configure(background = 'beige')
        self.root.title('Tetris');
        self.root.bind("<Down>",self.__down)
        self.root.bind("<Right>",self.__right)
        self.root.bind("<Left>",self.__left)
        self.root.bind("<Up>",self.__clockwise)
        self.root.bind("<space>",self.__downAll)
        self.root.bind("<Escape>", self.__pause)
        self.root.bind("<c>", self.__hold)
        self.root.bind("<C>", self.__hold)
        self.root.bind("<z>", self.__antiClockwise)
        self.root.bind("<Z>", self.__antiClockwise)
        self.board = [ [ None for i in range(10) ] for j in range(20) ]
        for i in range(0, 20):
            for j in range(0, 10):
                label = Label(self.root, width=4, height=2,relief=SOLID, border=1, background='white')
                label.grid(row=i, column=j)
                self.board[i][j] = label
        self.pause = False
        self.pauseLabel = Label(self.root, text="PAUSE", background="beige", foreground="red", font=("Verdana",18))
        self.pauseLabel.grid(row=10, column=20)
        self.pauseLabel.grid_remove()

        self.scoreTextLabel = Label(self.root, text="Score", background="beige", foreground="black", font=("Verdana",22))
        self.scoreTextLabel.grid(row=7, column=20)

        self.scoreLabel = Label(self.root, text="0", background="beige", foreground="black", font=("Verdana",19))
        self.scoreLabel.grid(row=8, column=20)

        self.nextLabel = Label(self.root, text="Next:", background="beige", foreground="black", font=("Verdana",18))
        self.nextLabel.grid(row=0, column=20)

        self.next1 = Label(self.root, width=4, height=2,relief=SOLID, border=1, background=self.colorsPieze[nextRandom])
        self.next1.grid(row=self.piezePosition[nextRandom][0][0], column=self.piezePosition[nextRandom][0][1])
        self.next2 = Label(self.root, width=4, height=2,relief=SOLID, border=1, background=self.colorsPieze[nextRandom])
        self.next2.grid(row=self.piezePosition[nextRandom][1][0], column=self.piezePosition[nextRandom][1][1])
        self.next3 = Label(self.root, width=4, height=2,relief=SOLID, border=1, background=self.colorsPieze[nextRandom])
        self.next3.grid(row=self.piezePosition[nextRandom][2][0], column=self.piezePosition[nextRandom][2][1])
        self.next4 = Label(self.root, width=4, height=2,relief=SOLID, border=1, background=self.colorsPieze[nextRandom])
        self.next4.grid(row=self.piezePosition[nextRandom][3][0], column=self.piezePosition[nextRandom][3][1])

        self.holdLabel = Label(self.root, text="Hold:", background="beige", foreground="black", font=("Verdana",18))
        self.holdLabel.grid(row=11, column=20)

        self.hold1 = Label(self.root, width=4, height=2,relief=SOLID, border=1, background=self.colorsPieze[0])
        self.hold1.grid(row=self.holdPosition[0][0][0], column=self.holdPosition[0][0][1])
        self.hold2 = Label(self.root, width=4, height=2,relief=SOLID, border=1, background=self.colorsPieze[0])
        self.hold2.grid(row=self.holdPosition[0][1][0], column=self.holdPosition[0][1][1])
        self.hold3 = Label(self.root, width=4, height=2,relief=SOLID, border=1, background=self.colorsPieze[0])
        self.hold3.grid(row=self.holdPosition[0][2][0], column=self.holdPosition[0][2][1])
        self.hold4 = Label(self.root, width=4, height=2,relief=SOLID, border=1, background=self.colorsPieze[0])
        self.hold4.grid(row=self.holdPosition[0][3][0], column=self.holdPosition[0][3][1])
    
    def __down(self, event):
        rule = "down(" + str(randint(0, 6)) + ")"
        self.__execute(rule)

    def __downAll(self, event):
        rule = "downAll(" + str(randint(0, 6)) + ")"
        self.__execute(rule)

    def __right(self, event):
        self.__execute("right")

    def __left(self, event):
        self.__execute("left")
    
    def __clockwise(self, event):
        self.__execute("clockwise")

    def __antiClockwise(self, event):
        self.__execute("antiClockwise")
    
    def __hold(self, event):
        self.__execute("hold")

    def __pause(self, event):
        if self.pause:
            self.pause = False
            self.pauseLabel.grid_remove()
            self.root.bind("<Down>",self.__down)
            self.root.bind("<Right>",self.__right)
            self.root.bind("<Left>",self.__left)
            self.root.bind("<Up>",self.__clockwise)
            self.root.bind("<space>",self.__downAll)
            self.root.bind("<c>", self.__hold)
            self.root.bind("<C>", self.__hold)
            self.root.bind("<z>", self.__antiClockwise)
            self.root.bind("<Z>", self.__antiClockwise)
            self.timer.start()
        else:
            self.pause = True
            self.pauseLabel.grid()
            self.root.unbind("<Down>")
            self.root.unbind("<Right>")
            self.root.unbind("<Left>")
            self.root.unbind("<Up>")
            self.root.unbind("<space>")
            self.root.unbind("<c>")
            self.root.unbind("<C>")
            self.root.unbind("<z>")
            self.root.unbind("<Z>")
            self.timer.stop()
    
    def __execute(self, rule):
        matrix,score,next, hold = self.performer.perform(rule)
        self.__updateTime(score)
        self.__paint(matrix, score, next, hold)

    def __updateTime(self, score):
        if score != self.score:
            if score == 0:
                time = 0.5
            elif score >= 1000 and score < 2000:
                time = 0.4
            elif score >= 2000 and score < 3000:
                time = 0.3
            elif score >= 3000 and score < 4000:
                time = 0.2
            elif score >= 4000:
                time = 0.1
            else:
                time = 0.5
            self.score = score
            if time != self.time:
                self.time = time
                self.timer.stop()
                self.timer = RepeatedTimer(self.time, self.__down, None)
    
    def __paint(self, board, score, next, hold):
        self.__paintNext(next=next)
        self.__paintHold(hold=hold)
        self.scoreLabel.configure(text=score)
        for i in range(0, 20):
            for j in range(0, 10):
                try:
                    color = self.colors[board[i][j]]
                    self.board[i][j].configure(background=color)
                except:
                    self.board[i][j].configure(background="white")
    def __paintHold(self, hold):
        self.hold1.configure(background=self.colorsPieze[hold])
        self.hold1.grid(row=self.holdPosition[hold][0][0], column=self.holdPosition[hold][0][1])
        self.hold2.configure(background=self.colorsPieze[hold])
        self.hold2.grid(row=self.holdPosition[hold][1][0], column=self.holdPosition[hold][1][1])
        self.hold3.configure(background=self.colorsPieze[hold])
        self.hold3.grid(row=self.holdPosition[hold][2][0], column=self.holdPosition[hold][2][1])
        self.hold4.configure(background=self.colorsPieze[hold])
        self.hold4.grid(row=self.holdPosition[hold][3][0], column=self.holdPosition[hold][3][1])

    def __paintNext(self, next):
        self.next1.configure(background=self.colorsPieze[next])
        self.next1.grid(row=self.piezePosition[next][0][0], column=self.piezePosition[next][0][1])
        self.next2.configure(background=self.colorsPieze[next])
        self.next2.grid(row=self.piezePosition[next][1][0], column=self.piezePosition[next][1][1])
        self.next3.configure(background=self.colorsPieze[next])
        self.next3.grid(row=self.piezePosition[next][2][0], column=self.piezePosition[next][2][1])
        self.next4.configure(background=self.colorsPieze[next])
        self.next4.grid(row=self.piezePosition[next][3][0], column=self.piezePosition[next][3][1])