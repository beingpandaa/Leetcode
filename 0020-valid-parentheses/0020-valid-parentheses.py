class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ele in s:
            if ele in ("{","(","["):
                stack.append(ele)
            else:
                if len(stack)>0 and ((ele == "]" and stack[-1] =="[") or (ele == ")" and stack[-1] =="(") or (ele == "}" and stack[-1] =="{")) :
                    stack.pop()
                else:
                    return False

        return len(stack)==0