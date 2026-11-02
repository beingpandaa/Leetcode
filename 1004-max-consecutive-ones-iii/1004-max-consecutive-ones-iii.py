class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        l,r = 0,0
        ans = 0
        curr = 0
        numZero = 0
        while r<n:

            if nums[r] == 0:
                if numZero<k:
                    numZero += 1
                    ans = max(ans,r-l+1)
                    r+=1
                else:
                    if l<r:
                        if nums[l]==0:
                            numZero-=1
                        l+=1
                    else:
                        r+=1
                        l+=1
            else:
                ans = max(ans,r-l+1)
                r+=1
        return ans