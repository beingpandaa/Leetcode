class Solution:
    def getParenthesis(self,res,openB,closeB,curr = []):
        if not openB and not closeB:
            s = "".join(curr)
            res.append(s)
            return
        if openB>0:
            curr.append("(")
            self.getParenthesis(res,openB-1,closeB,curr)
            curr.pop()
        if closeB > openB:
            curr.append(")")
            self.getParenthesis(res,openB,closeB-1,curr)
            curr.pop()

    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        self.getParenthesis(res,n,n)
        return res


        