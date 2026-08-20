class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        lfirst=0
        lsec=1
        while lsec!=len(nums)-1:
            if nums[lfirst]>nums[lsec]:
                index = lsec+1
                while index!=lfirst+1:
                    nums[index-1]+=nums[index]
                    nums[index]=nums[index-1]-nums[index]
                    nums[index-1]-=nums[index]
                    index-=1
                lfirst+=1
            lsec+=1
        return nums

        