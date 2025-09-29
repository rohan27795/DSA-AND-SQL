class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [["."] * n for _ in range(n)]
        res = []

        def is_safe(board,row,col,n):

            for i in range(row):
                if board[i][col] == "Q":  # check upper column
                    return False

            i,j = row-1,col-1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":     #check upper left diagonal
                    return False
                i -=1
                j -=1
            i,j = row-1,col+1      
            while i >= 0 and j < n:
                if board[i][j] == "Q":      #check upper right diagonal
                    return False
                i -=1
                j +=1

            return True

        def Nqueen(board,row,n,res):
            if row == n:
                res.append(["".join(r) for r in board])
            for col in range(n):
                if is_safe(board,row,col,n):
                    board[row][col] = "Q"
                    Nqueen(board,row+1,n,res)   #recuse every row
                    board[row][col] = "."       #backtrack

        Nqueen(board,0,n,res)
        return res

            
        




            

            

        
        