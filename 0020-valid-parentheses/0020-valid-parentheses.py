class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ele in s:
            if ele=='[' or ele=='(' or ele=='{':stack.append(ele)
            elif ele==']':
                if not stack or stack[-1]!='[':return False
                else:
                    stack.pop()
            elif ele==')':
                if not stack or stack[-1]!='(':return False
                else:
                    stack.pop()
            elif ele=='}':
                if not stack or stack[-1]!='{':return False
                else:
                    stack.pop()
        return stack==[]
            
                