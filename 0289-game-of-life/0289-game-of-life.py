class Solution:
    def checklive(self,board,i,j,n,m):
        count=0
        if i+1<n and (board[i+1][j]==1 or board[i+1][j]=='zindatha_ab_margya'):
            count+=1
        if i-1>=0 and (board[i-1][j]==1 or board[i-1][j]=='zindatha_ab_margya'):
            count+=1
        if i+1<n and j+1<m and (board[i+1][j+1]==1 or board[i+1][j+1]=='zindatha_ab_margya'):
            count+=1
        if i-1>=0 and j-1>=0 and (board[i-1][j-1]==1 or board[i-1][j-1]=='zindatha_ab_margya'):
            count+=1
        if j+1<m and (board[i][j+1]==1 or board[i][j+1]=='zindatha_ab_margya'):
            count+=1
        if j-1>=0 and (board[i][j-1]==1 or board[i][j-1]=='zindatha_ab_margya'):
            count+=1
        if i+1<n and j-1>=0 and (board[i+1][j-1]==1 or board[i+1][j-1]=='zindatha_ab_margya'):
            count+=1
        if j+1<m and i-1>=0 and (board[i-1][j+1]==1 or board[i-1][j+1]=='zindatha_ab_margya'):
            count+=1
            
        return count
       
            
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        for i in range(n):
            for j in range(m):
                
                count=self.checklive(board,i,j,n,m)
                if board[i][j]==0:
                    if count==3:
                        board[i][j]='abhi_zinda_hua'
                else:
                    if count<2 or count>3:
                        board[i][j]='zindatha_ab_margya'
        for i in range(n):
            for j in range(m):
                if board[i][j]=='zindatha_ab_margya':
                    board[i][j]=0
                if board[i][j]=='abhi_zinda_hua':
                    board[i][j]=1
        return board