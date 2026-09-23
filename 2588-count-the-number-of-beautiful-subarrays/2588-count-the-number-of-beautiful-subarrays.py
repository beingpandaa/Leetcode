class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        d={0:1}
        curr = 0
        count = 0 
        for ele in nums:
            curr = curr^ele
            if curr not in d :
                d[curr] = 1
            else:
                count += d[curr]
                d[curr] += 1
        return count

