class Solution:
    def helper(self,nums,i,d,deepee):
        if i==len(nums)-1:return nums[i]*d[nums[i]]
        if i==len(nums):return 0
        
        #first lets consider the call where we are not considering the ith call
        if deepee[i+1]==-1:deepee[i+1]=self.helper(nums,i+1,d,deepee)
        ans2=deepee[i+1]
        
        
        #now lets start considering ith element, then we have two possibilities 
        ans1=nums[i]*d[nums[i]]
        #standing at ith, if next element is adjacent to the value of current ith element then we cant include the next element even if we want to. So we'll ask recursion to give us the max we can get starting from i+2th position and add our current value to that 
        if nums[i+1]==nums[i]+1:
            
            if deepee[i+2]==-1:deepee[i+2]=self.helper(nums,i+2,d,deepee)
            ans1+=deepee[i+2]
            return max(ans1,ans2)
        
        #in either case we dont care that if the next element is included or not because even if its included, we can include ith element then too because its not adjacent to the next element , so whatsoever i+1 yeilds us, we can simply include our answer to that and return that as the answer
        else:
            return ans1+ans2
        
        
    def deleteAndEarn(self, nums: List[int]) -> int:
        d=Counter(nums)
        nums=sorted(list(set(nums)))
        deepee=[-1 for i in range(len(nums)+1)]
        return self.helper(nums,0,d,deepee)