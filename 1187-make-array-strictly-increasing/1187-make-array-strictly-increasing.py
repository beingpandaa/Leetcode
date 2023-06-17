class Solution:
    def dfs(self,i,arr1,arr2,prev,dp):
        if i==len(arr1):return 0
        dp[(prev,i)]=sys.maxsize
        if arr1[i]>prev:
            if (arr1[i],i+1) not in dp:dp[(arr1[i],i+1)]=self.dfs(i+1,arr1,arr2,arr1[i],dp)
            dp[(prev,i)]=dp[(arr1[i],i+1)]
        index=bisect.bisect_right(arr2, prev)
        if index<len(arr2):
            if (arr2[index],i+1) not in dp:dp[(arr2[index],i+1)]=self.dfs(i+1,arr1,arr2,arr2[index],dp)
            dp[(prev,i)]=min(dp[(prev,i)],1+dp[(arr2[index],i+1)])
        return dp[(prev,i)]
        
        
        
        
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {}
        arr2.sort()
        res=self.dfs(0,arr1,arr2,-1,{})
        return res if res<sys.maxsize else -1
        
        