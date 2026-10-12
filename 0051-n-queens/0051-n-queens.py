class Solution:
    def isSafe(self, board, row, col, n):
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def createBoard(self,n):
        row = ["." for i in range(n)]
        return [row[:] for i in range(n)]

    def convertBoard(self, board):
        return ["".join(row) for row in board]
    
    def appendBoards(self,board,ans,n,currRow = 0):
        if currRow == n:
            ans.append(self.convertBoard(board))
            return
        for j in range(n):
            if self.isSafe(board,currRow,j,n):
                board[currRow][j]="Q"
                self.appendBoards(board,ans,n,currRow+1)
                board[currRow][j]="."


    def solveNQueens(self, n: int) -> list[list[str]]:
        board = self.createBoard(n)
        ans = []
        self.appendBoards(board,ans,n)
        return ans

        