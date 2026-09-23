class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        d = {0:-1}
        target = sum(nums)-x
        if target == 0 : return len(nums)
        curr = 0
        maxlen = 0
        for i in range(len(nums)):
            curr +=nums[i]
            if curr-target in d:
                maxlen = max(maxlen,i-d[curr-target])
            if curr not in d:
                d[curr] = i
        if maxlen==0: return -1
        return len(nums)-maxlen
        
        