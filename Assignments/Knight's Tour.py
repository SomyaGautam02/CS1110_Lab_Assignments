#Name-Somya Gautam
#Roll Number- 2020BTechCSE076
#Batch-A

# Knight's Tour

moveRow = [2,1,-1,-2,-2,-1,1,2]
moveCol = [1,2,2,1,-1,-2,-2,-1]
class KnightTour:   
    def StartTour(self,chessboard, row, col, move):
        if(move == 64):
            for i in range(8):
                for j in range(8):
                    if(chessBoard[i][j] < 10):
                        chessBoard[i][j] = str("0" + str(chessBoard[i][j]))
                    print(f"{chessBoard[i][j]} ",end=" ")
                print()
            return True
        else:
            for i in range(len(moveRow)):
                newRow = row + moveRow[i]
                newCol = col + moveCol[i]
                if(self.ifValidMove(chessBoard,newRow,newCol)):
                    move+=1
                    chessBoard[newRow][newCol] = move
                    if(self.StartTour(chessBoard,newRow,newCol,move)):
                        return True
                    move-=1
                    chessBoard[newRow][newCol]=0 
        return False

    def ifValidMove(self,chessBoard,newRow,newCol):
        if((newRow >= 0) and (newRow < 8) and (newCol >= 0) and (newCol < 8) and (chessBoard[newRow][newCol]==0)):
            return True
        return False

chessBoard = [[0 for i in range(8)] for j in range(8)]
chessBoard[1][1] = 1      
executer=KnightTour()
executer.StartTour(chessBoard,0,0,1)
