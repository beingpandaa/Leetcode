class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        def dfs(i,j,itr=0):
            if i<0 or i==m or j<0 or j==n or board[i][j]!=word[itr]:
                return False
            if itr==len(word)-1:
                return True 
            ele=board[i][j]
            board[i][j]='0'
            ans1=dfs(i+1,j,itr+1)
            ans2=dfs(i,j+1,itr+1)
            ans3=dfs(i-1,j,itr+1)
            ans4=dfs(i,j-1,itr+1)
            board[i][j]=ele
            
            
            return ans1 or ans2 or ans3 or ans4
        
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j):
                        print(i,j)
                        return True
        return False
        
        
            
        