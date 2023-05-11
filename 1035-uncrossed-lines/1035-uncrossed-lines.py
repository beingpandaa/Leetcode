class Solution:
    def helper(self,i,j,nums1,nums2,dp):
        if i==len(nums1) or j==len(nums2):return 0
        if nums1[i]==nums2[j]:
            if dp[i+1][j+1]==-1:dp[i+1][j+1]=self.helper(i+1,j+1,nums1,nums2,dp)
            return 1+dp[i+1][j+1]
        if dp[i][j+1]==-1:dp[i][j+1]=self.helper(i,j+1,nums1,nums2,dp)
        if dp[i+1][j]==-1:dp[i+1][j]=self.helper(i+1,j,nums1,nums2,dp)
        return max(dp[i][j+1],dp[i+1][j])
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[-1 for i in range(len(nums2)+1)]for j in range(len(nums1)+1)]
        return self.helper(0,0,nums1,nums2,dp)