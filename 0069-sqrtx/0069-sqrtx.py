class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0 
        high = x
        while low <= high:
            mid = low+(high-low)//2
            val = mid*mid
            if val>x:high = mid-1
            elif val<x:low = mid+1
            else:return mid
        return high
        