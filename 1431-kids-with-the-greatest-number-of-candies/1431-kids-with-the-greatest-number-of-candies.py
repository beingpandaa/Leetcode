class Solution:
    def kidsWithCandies(self, arr: List[int], extra: int) -> List[bool]:
        ma=max(arr)
        for i in range(len(arr)):arr[i]=(arr[i]+extra)>=ma
        return arr
            