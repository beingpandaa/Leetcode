class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low=0
        high=len(letters)-1
        target=ord(target)
        if ord(letters[high])<=target:return letters[low]
        while low<high:
            mid=(low+high)//2
            if ord(letters[mid])<=target:
                low=mid+1
            elif ord(letters[mid])>target:
                high=mid
            # print(low,high)
        return letters[low]
    
            