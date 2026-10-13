class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
        score = 0
        nums.sort()
        i,j=0,len(nums)-1
        while i<=j:
            if i==j:
                score+=nums[i]**2
            else:
                score+=(nums[j]**2)-(nums[i]**2)
            i+=1
            j-=1
        return score
        
        