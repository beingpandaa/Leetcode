class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        score = 0
        for i in range(len(nums)):nums[i]=nums[i]**2
        nums.sort()
        i,j=0,len(nums)-1
        while i<=j:
            if i==j:
                score+=nums[i]
            else:
                score+=(nums[j])-(nums[i])
            i+=1
            j-=1
        return score
        
        