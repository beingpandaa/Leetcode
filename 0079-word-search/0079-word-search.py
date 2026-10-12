class Solution:
    def searchWord(self,board,word,i=0,j=0,index=0):
        if index == len(word):return True
        if i<0 or i==len(board) or j<0 or j==len(board[0]) or board[i][j]=="*" or board[i][j]!=word[index]: return False
        temp = board[i][j] 
        board[i][j]="*"
        op1 = self.searchWord(board,word,i+1,j,index+1)
        op2 = self.searchWord(board,word,i-1,j,index+1)
        op3 = self.searchWord(board,word,i,j+1,index+1)
        op4 = self.searchWord(board,word,i,j-1,index+1)
        board[i][j] =temp
        return op1 or op2 or op3 or op4

    def exist(self, board: list[list[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                     if self.searchWord(board,word,i,j)==True:
                        print(i,j)
                        return True
        return False 
        