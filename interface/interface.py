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
        self.timer = RepeatedTimer(0.7, self.__down, None)
        self.performer = TetrisPerformer(initialRandom=randint(0, 6))
        self.colors = dict({"empty": "white", "iType": "cyan", "jType": "blue", "lType": "orange", "oType": "yellow", "sType": "green", "zType": "red", "tType": "magenta"}) 
        self.__initWindow()
        self.root.mainloop()

    def __initWindow(self):
        self.root.geometry('485x720')
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
                label = Label(self.root, width=4, height=2,relief=SOLID, border=1, background='white')
                label.grid(row=i, column=j)
                self.board[i][j] = label
        self.pause = False
        self.pauseLabel = Label(self.root, text="PAUSA", background="beige", foreground="black", font=("Verdana",22))
        self.pauseLabel.grid(row=10, column=20)
        self.pauseLabel.grid_remove()

        self.scoreTextLabel = Label(self.root, text="Score", background="beige", foreground="black", font=("Verdana",22))
        self.scoreTextLabel.grid(row=7, column=20)

        self.scoreLabel = Label(self.root, text="0", background="beige", foreground="black", font=("Verdana",19))
        self.scoreLabel.grid(row=8, column=20)
    
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
            self.root.bind("<Down>",self.__down)
            self.root.bind("<Right>",self.__right)
            self.root.bind("<Left>",self.__left)
            self.root.bind("<Up>",self.__clockwise)
            self.root.bind("<space>",self.__downAll)
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
        matrix, score = self.performer.perform(rule)
        self.__paint(matrix, score)
    
    def __paint(self, board, score):
        self.scoreLabel.configure(text=score)
        for i in range(0, 20):
            for j in range(0, 10):
                self.board[i][j].configure(background=self.colors[board[i][j]])


