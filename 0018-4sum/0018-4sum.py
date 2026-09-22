class Solution:
    def twoSum(self,nums,i,target):
        j = len(nums)-1
        op = []
        while i <j:
            

            curr = nums[i]+nums[j]
            if curr>target:
                j-=1
            elif curr<target:
                i+=1
            else:
                op.append([nums[i],nums[j]])
                while i<j and nums[i+1]==nums[i]:i+=1
                while i<j and nums[j-1]==nums[j]:j-=1
                i+=1
                j-=1
        return op

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i>0 and nums[i-1]==nums[i]:continue
            else:
                for j in range(i+1,len(nums)-2):
                    if j>i+1 and nums[j-1]==nums[j]:
                        continue
                    else:
                        op = self.twoSum(nums,j+1,target-nums[i]-nums[j])
                        for ele in op :
                            res.append([nums[i],nums[j],ele[0],ele[1]])
        return res
