class Solution:
    
    def lcs(self,str1,str2):
        n=len(str1)
        m=len(str2)

        dp=[[0 for i in range (m+1)]for j in range (n+1)]
        count=0
        for i in range (n-1,-1,-1):
            for j in range (m-1,-1,-1):

                if str1[i]==str2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                    count=max(count,dp[i][j])
                else:
                    dp[i][j] = 0
        return count
        
        
        
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        return self.lcs(nums1,nums2)