class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        major1 = -sys.maxsize
        major2 = -sys.maxsize
        count1,count2=0,0
        for ele in nums:
            if count1==0 and major2!=ele:
                count1 = 1
                major1 = ele
            elif count2==0 and major1!=ele:
                count2=1
                major2 = ele
            elif ele == major1:count1+=1
            elif ele == major2:count2+=1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for ele in nums:
            if ele==major1:count1+=1
            elif ele==major2:count2+=1
        majorFreq = len(nums)//3
        arr=[]
        if count1>majorFreq:arr.append(major1)
        if count2>majorFreq:arr.append(major2)
        arr.sort()
        return arr