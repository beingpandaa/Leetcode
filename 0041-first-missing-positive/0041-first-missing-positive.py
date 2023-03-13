class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_missing=len(nums)+1
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if index>=0 and index<len(nums):
                if nums[index]==0:
                    nums[index]=-(index+1)  
            #what we are trying to do here is that, we are directed to an index where value is 0,now we cant change the                                                  value 0 to negative as - 0 is 0 nly also we cant cchange it to a random number as it can also lead to direction                                              to a random index so we assign it a value which will direct it to the same index again or we can change it to a                                              value which is out of bound of our search space.
                else:
                    nums[index]=-abs(nums[index])
                
        for i in range(1,max_missing):
            index=i-1
            if nums[index]>=0:return i
        return max_missing
            
            