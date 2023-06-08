class Solution:
    def binSearch(self,low,high,row,grid):
        # if we are to search in column, we gonna set flag True else, we gonna set it False.
        if grid[row][low]<0:return -1
        while low<high:
            mid=(low+high+1)//2
            if grid[row][mid]>-1:
                low=mid
            elif grid[row][mid]<=-1:
                high=mid-1
        return low
            
            
            
    def countNegatives(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        count=0
        for row in range(n):
            col=self.binSearch(0,m-1,row,grid)
            if col==-1:
                count+=(n-row)*m
                break
            count+=m-1-col
        return count
        