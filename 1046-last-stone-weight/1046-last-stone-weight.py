class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones)>1:
            p=heapq._heappop_max(stones)
            q=heapq._heappop_max(stones)
            if p-q!=0:
                stones.append(p-q)
                heapq._heapify_max(stones)
        if len(stones)==0:return 0  
        return stones[0]
        
        