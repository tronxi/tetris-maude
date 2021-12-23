from tkinter import *
import maude
from random import seed
from random import randint
from repeatedTimer import RepeatedTimer

class Interface():
    def __init__(self):
        maude.init()
        maude.load("../logic/loads.maude")
        self.root = Tk()
        self.root.geometry('420x760')
        self.root.configure(background = 'beige')
        self.root.title('Tetris');
        self.root.bind("<Down>",self.down)
        self.root.bind("<Right>",self.right)
        self.root.bind("<Left>",self.left)
        self.root.bind("<space>",self.downAll)
        self.initialTerm = "{ < ${board} > | ${rule} }"
        self.maudeBoard = "[(21, 21) | inactive] / randomPiece(" + str(randint(0, 6)) + ")"
        self.tetris = maude.getModule('TETRIS')
        self.timer = RepeatedTimer(1, self.down, None)
        seed(1)
        self.board = [ [ None for i in range(10) ] for j in range(20) ]
        for i in range(0, 20):
            for j in range(0, 10):
                label = Label(self.root, width=4, height=2,relief=SOLID, background='white')
                label.grid(row=i, column=j)
                self.board[i][j] = label
        self.root.mainloop()
    
    def down(self, event):
        rule = "down(" + str(randint(0, 6)) + ")"
        self.execute(rule)

    def downAll(self, event):
        rule = "downAll(" + str(randint(0, 6)) + ")"
        self.execute(rule)

    def right(self, event):
        self.execute("right")

    def left(self, event):
        self.execute("left")
    
    def execute(self, rule):
        term = self.initialTerm.replace("${board}", self.maudeBoard).replace("${rule}", rule)
        parseTerm = self.tetris.parseTerm(term)
        parseTerm.rewrite(1)
        self.maudeBoard = self.termToBoard(parseTerm)
        self.paint(self.boardToMatrix(self.maudeBoard))

    def termToBoard(self, term):
        term = str(term)
        return term[term.find("<")+len("<"):term.rfind(">")]
    
    def boardToMatrix(self, board):
        newBoard = [ [ None for i in range(10) ] for j in range(20) ]
        pieces = board.split("/")
        for piece in pieces:
            pieceSplit = piece.split("|")
            status = pieceSplit[1].replace(" ", "").replace("]", "")
            positions = pieceSplit[0].replace(" ", "").replace("[", "").split("\\")
            for position in positions:
                if position != "emptyPositionList" and not position.startswith("if"):
                    x, y = position.replace("(", "").replace(")", "").split(",")
                    x = int(x)
                    y = int(y)
                    if x <= 19 and y <= 9:
                        newBoard[x][y] = status
        return newBoard
    
    def paint(self, board):
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


