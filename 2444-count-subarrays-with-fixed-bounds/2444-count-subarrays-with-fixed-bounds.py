class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxk: int) -> int:
        off=mi=ma=-1
        count=0
        for i in range(len(nums)):
            if nums[i]<mink or nums[i]>maxk:off=i
            if nums[i]==mink:mi=i
            if nums[i]==maxk:ma=i
            count+=max(0,min(mi,ma)-off)
        return count
        