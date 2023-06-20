class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        window_size=1+2*k
        op=[]
        curr=0
        for i in range(len(nums)):
            nums[i]+=curr
            curr=nums[i]
        i=0
        while i<len(nums):
            if i<k or i>=len(nums)-k:
                op.append(-1)
            else:
                index=i+k
                # print(index)
                if index==window_size-1:op.append(nums[index]//window_size)
                else:op.append((nums[index]-nums[index-window_size])//window_size)
            i+=1
        # print(nums)
        return op
            
                