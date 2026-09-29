class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        if (len(grid) + len(grid[0]) - 1) % 2 == 1:return False
        d={}
        def dfs(i=0,j=0,balance=0):
            if i == len(grid) or j == len(grid[0]):return False
            if grid[i][j]=='(':balance+=1
            if grid[i][j]==')':balance-=1
            if balance<0:return False
            if i == len(grid)-1 and j == len(grid[0])-1 and balance==0 :return True
            if (i+1,j,balance) not in d: d[(i+1,j,balance)] = dfs(i+1,j,balance)
            if (i,j+1,balance) not in d: d[(i,j+1,balance)] = dfs(i,j+1,balance) 
            return  d[(i+1,j,balance)] or d[(i,j+1,balance)]
        return dfs()