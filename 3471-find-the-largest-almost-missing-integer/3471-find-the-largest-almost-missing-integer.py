class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):return max(nums)
        d={}
        for ele in nums:
                d[ele]=d.get(ele,0)+1
        if k == 1:
            maxNum=-1
            for ele in d:
                if d[ele]==1:maxNum=max(maxNum,ele)
            return maxNum
        else:
            if d[nums[0]]==1 and d[nums[-1]]==1 : return max(nums[0],nums[-1])
            elif d[nums[0]]!=1 and d[nums[-1]]!=1:return -1
            return nums[0] if d[nums[0]]==1 else nums[-1]

        

