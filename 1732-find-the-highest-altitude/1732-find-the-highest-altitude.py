class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count=0
        val=0
        for ele in gain:
            count+=ele
            val=max(count,val)
        return val