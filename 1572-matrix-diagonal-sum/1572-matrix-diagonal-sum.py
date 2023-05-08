class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        ans=0
        for i in range(len(mat)):
            ans+=mat[i][i]+mat[i][n-1-i]
        return ans-(mat[n//2][n//2] if n%2 else 0)
            
            
           