class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        op = []
        for i in range(len(nums)):
            if nums[i]==target:
                op.append(i)
            else:
                if op:return op
        return op
            