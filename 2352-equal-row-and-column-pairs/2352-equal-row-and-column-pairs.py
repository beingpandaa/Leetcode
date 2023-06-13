class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d={}
        n=len(grid)
        count=0
        
        for row in grid:
            s=''.join([str(ele)+' ' for ele in row])
            d[s]=d.get(s,0)+1
       
        for j in range(n):
            s=''
            for i in range(n):
                s+=str(grid[i][j])+' '
          
            count+=d.get(s,0)
        return count
            