import maude
from interface.parser import Parser

class TetrisPerformer():
    def __init__(self, initialRandom, nextRandom):
        maude.init()
        maude.load("logic/loads.maude")
        self.tetris = maude.getModule('TETRIS')
        self.initialTerm = "{ < ${board} > | ${rule} }"
        initialBoard = self.tetris.parseTerm("initialBoard(" + str(initialRandom) + "," + str(nextRandom) + ")")
        initialBoard.reduce()
        self.maudeBoard = str(initialBoard)
        self.lastMaudeBoard = str(initialBoard)
        self.parser = Parser()

    def perform(self, rule):
        term = self.initialTerm.replace("${board}", self.maudeBoard).replace("${rule}", rule)
        parseTerm = self.tetris.parseTerm(term)
        parseTerm.rewrite(1)
        self.lastMaudeBoard = self.maudeBoard
        try:
            self.maudeBoard = self.parser.termToBoard(parseTerm)
            return self.parser.boardToMatrix(self.maudeBoard)
        except:
            self.maudeBoard = self.lastMaudeBoard
            return self.parser.boardToMatrix(self.maudeBoard)