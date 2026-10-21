class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low , high, ans = 0, len(nums)-1 , sys.maxsize

        while low <= high :
            mid = low+ (high - low)//2

            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                ans = min(ans,nums[mid])
                low +=1
                high -=1

            elif nums[low] <= nums[mid]:
                ans = min(nums[low],ans)
                low = mid + 1

            else:
                ans = min(nums[mid],ans)
                high = mid - 1
        return ans