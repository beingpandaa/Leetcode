class Solution:
    def reverseArray(self,nums,start):
        end = len(nums)-1
        while start<end:
            nums[start]+=nums[end]
            nums[end]=nums[start]-nums[end]
            nums[start]-=nums[end]
            start+=1
            end -=1


    def findJustGreater(self,left,nums,target):
        right = len(nums)-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<=target:
                right = mid-1
            else:
                left = mid+1
        return right 

    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                JustGreaterIndex = self.findJustGreater(i,nums,nums[i-1])
                nums[i-1],nums[JustGreaterIndex] = nums[JustGreaterIndex], nums[i-1]
                self.reverseArray(nums,i)
                return nums
        self.reverseArray(nums,0)
        return nums

                
                