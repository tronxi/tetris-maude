import maude
from interface.parser import Parser

class TetrisPerformer():
    def __init__(self, initialRandom):
        maude.init()
        maude.load("logic/loads.maude")
        self.tetris = maude.getModule('TETRIS')
        self.initialTerm = "{ < ${board} > | ${rule} }"
        self.maudeBoard = "randomPiece(" + str(initialRandom) + ")"
        self.parser = Parser()

    def perform(self, rule):
        term = self.initialTerm.replace("${board}", self.maudeBoard).replace("${rule}", rule)
        parseTerm = self.tetris.parseTerm(term)
        parseTerm.rewrite(1)
        self.maudeBoard = self.parser.termToBoard(parseTerm)
        return self.parser.boardToMatrix(self.maudeBoard)