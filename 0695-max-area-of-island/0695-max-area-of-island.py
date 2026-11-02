class Solution:
    def dfs(self,grid,i,j):
        if i<0 or i >=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0 :
            return 0
        grid[i][j]=0
        area=1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for di, dj in directions:
            area += self.dfs(grid, i + di, j + dj)
        return area

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area=max(area,self.dfs(grid,i,j))
        return area
                