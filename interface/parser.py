class Parser():

    def termToBoard(self, term):
        term = str(term)
        return term[term.find("<")+len("<"):term.rfind(">")]
    
    def boardToMatrix(self, board):
        newBoard = [ [ "empty" for i in range(10) ] for j in range(20) ]
        pieces = board.split("/")
        score = 0
        next = 0
        hold = 0
        for piece in pieces:
            if "hold" in piece:
                try:
                    hold = int(piece.replace(" ", "").replace("hold(", "").replace(")", ""))
                    continue
                except:
                    print("error")
                    continue
            if "score" in piece:
                try:
                    score = int(piece.replace(" ", "").replace("score(", "").replace(")", ""))
                    continue
                except:
                    print("error")
                    continue
            if "next" in piece:
                try:
                    next = int(piece.replace(" ", "").replace("next(", "").replace(")", ""))
                    continue
                except:
                    print("error")
                    continue
            pieceSplit = piece.split("|")
            positions = pieceSplit[0].replace(" ", "").replace("[", "").split("\\")
            type = pieceSplit[2].replace(" ", "").replace("]", "")
            for position in positions:
                if position != "emptyPositionList" and  position.startswith("("):
                    try:
                        x, y = position.replace("(", "").replace(")", "").split(",")
                        x = int(x)
                        y = int(y)
                        newBoard[x][y] = type
                    except:
                        print("error")
        return newBoard, score, next, hold