class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        j=0
        i=0
        while i<len(popped):
            stack.append(pushed[i])
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
            i+=1
        return j==len(popped)
            
            
            
            
            
            
                
        