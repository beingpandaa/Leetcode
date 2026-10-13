class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        score = 0
        for i in range(len(nums)):nums[i]=nums[i]**2
        nums.sort()
        mid_index = len(nums)//2
        return sum(nums[mid_index:])-sum(nums[:mid_index])
      
        
        