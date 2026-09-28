class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ele in s:
            if ele == ")":
                li = []
                while stack[-1] != "(":
                    li.append(stack.pop())
                stack.pop()
                stack.extend(li)
            else:
                stack.append(ele)
        return "".join(stack)