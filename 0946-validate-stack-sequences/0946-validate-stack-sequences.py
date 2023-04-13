class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        z=0
        i=0
        while i<len(popped):
            stack.append(pushed[i])
            while stack and stack[-1]==popped[z]:
                stack.pop()
                z+=1
            i+=1
        return z==len(popped)
            
            
            
            
            
            
                
        