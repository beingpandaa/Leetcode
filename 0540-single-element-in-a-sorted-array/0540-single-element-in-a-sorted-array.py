class Solution(object):
    def singleNonDuplicate(self, nums):
        low , high = 0 , len(nums)-1
        while low <= high :
            mid = low+ (high-low)//2
            left = mid!=0 and nums[mid-1]==nums[mid]
            right = mid!=len(nums)-1 and nums[mid+1]==nums[mid]
            if left :
                if (high-mid)%2==0:
                    high = mid-2
                else:
                    low = mid+1
            elif right:
                if (high-mid+1)%2==0:
                    high = mid-1
                else:
                    low = mid+2
            else:
                return nums[mid]


        