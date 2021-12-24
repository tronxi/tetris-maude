class Parser():

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
                if position != "emptyPositionList" and  position.startswith("("):
                    x, y = position.replace("(", "").replace(")", "").split(",")
                    x = int(x)
                    y = int(y)
                    newBoard[x][y] = status
        return newBoard