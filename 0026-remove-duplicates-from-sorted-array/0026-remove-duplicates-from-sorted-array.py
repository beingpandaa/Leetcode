class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos=0
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[pos]=nums[i-1]
                pos+=1
        nums[pos]=nums[-1]
        return pos+1