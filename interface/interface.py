from tkinter import *
from interface.repeatedTimer import RepeatedTimer
from interface.tetrisPerformer import TetrisPerformer
from random import randint
from random import seed
import time

class Interface():
    def __init__(self):
        self.root = Tk()
        seed(int(time.time() * 1000))
        self.timer = RepeatedTimer(0.7, self.__down, None)
        self.performer = TetrisPerformer(initialRandom=randint(0, 6))
        self.__initWindow()
        self.root.mainloop()

    def __initWindow(self):
        self.root.geometry('500x760')
        self.root.configure(background = 'beige')
        self.root.title('Tetris');
        self.root.bind("<Down>",self.__down)
        self.root.bind("<Right>",self.__right)
        self.root.bind("<Left>",self.__left)
        self.root.bind("<Up>",self.__clockwise)
        self.root.bind("<space>",self.__downAll)
        self.root.bind("<Escape>", self.__pause)
        self.board = [ [ None for i in range(10) ] for j in range(20) ]
        for i in range(0, 20):
            for j in range(0, 10):
                label = Label(self.root, width=4, height=2,relief=SOLID, background='white')
                label.grid(row=i, column=j)
                self.board[i][j] = label
        self.pause = False
        self.pauseLabel = Label(self.root, text="PAUSA", background="beige", foreground="black", font=("Verdana",22))
        self.pauseLabel.grid(row=10, column=20)
        self.pauseLabel.grid_remove()
    
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

    def __pause(self, event):
        if self.pause:
            self.pause = False
            self.pauseLabel.grid_remove()
            self.root.bind("<Down>",self.down)
            self.root.bind("<Right>",self.right)
            self.root.bind("<Left>",self.left)
            self.root.bind("<Up>",self.clockwise)
            self.root.bind("<space>",self.downAll)
            self.timer.start()
        else:
            self.pause = True
            self.pauseLabel.grid()
            self.root.unbind("<Down>")
            self.root.unbind("<Right>")
            self.root.unbind("<Left>")
            self.root.unbind("<Up>")
            self.root.unbind("<space>")
            self.timer.stop()
    
    def __execute(self, rule):
        matrix = self.performer.perform(rule)
        self.__paint(matrix)
    
    def __paint(self, board):
        for i in range(0, 20):
            for j in range(0, 10):
                label = self.board[i][j]
                if board[i][j]:
                    if board[i][j] == "inactive":
                        label.configure(background='grey')
                    else:
                        label.configure(background='blue')
                else:
                    label.configure(background='white')


