class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i,curr=1,0
        missing=0
        while missing <=k:
            if curr<len(arr) and i==arr[curr]:
                curr+=1
            else:
                missing+=1
            if missing==k:return i
            i+=1
            