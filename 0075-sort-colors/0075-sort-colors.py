class Solution:
    def sortColors(self, nums: list[int]) -> None:
        captureZero = 0
        captureTwo = len(nums)-1
        i=0
        while i<=captureTwo:
            match nums[i]:
                case 2:
                    nums[i], nums[captureTwo] = nums[captureTwo], nums[i]
                    captureTwo -=1
                case 0:
                    nums[i], nums[captureZero] = nums[captureZero], nums[i]
                    captureZero +=1
                    i+=1
                case 1:
                    i+=1
            
        
        