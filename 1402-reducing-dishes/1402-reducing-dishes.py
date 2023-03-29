class Solution:
    def maxSatisfaction(self, arr: List[int]) -> int:
        n=len(arr)
        arr.sort()
        total=arr[n-1]*n
        
        for i in range(n-2,-1,-1):
            
            total+=arr[i]*(i+1)
            arr[i]+=arr[i+1]
        i=0
        while i<n and total<total-arr[i] :
            total=total-arr[i]
            i+=1
        if i==n:return 0
        return total
            
            
        
        
        
        
        