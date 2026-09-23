class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        d={0:1}
        curr = 0
        count = 0 
        for ele in nums:
            curr = curr^ele
            d[curr] = d.get(curr,0) + 1
            count += d[curr]-1
        return count

