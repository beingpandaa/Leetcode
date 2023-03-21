class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        res=0
        while i <n:
            if nums[i]==0:
                count=1
                while i+1<n and nums[i+1]==0:
                    count+=1
                    i+=1
                # print(count)
                res+=(count+1)*(count)//2
                
                
                
            i+=1
        return res
        