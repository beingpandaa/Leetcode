class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def func(heights):
            stack=[]
            ps=[]
            ns=[0]*len(heights)
            for i in range(len(heights)):
                while stack and heights[stack[-1]]>=heights[i]:
                            stack.pop()
                if stack:
                    ps.append(stack[-1])
                else:
                    ps.append(-1)
                stack.append(i)
            stack.clear()
            for i in range(len(heights)-1,-1,-1):
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if stack:
                    ns[i]=stack[-1]
                else:
                    ns[i]=len(heights)

                stack.append(i)
            ar=0
            for i in range(len(heights)):
                ar=max(ar,(ns[i]-ps[i]-1)*heights[i])
            return ar
        n=len(matrix)
        m=len(matrix[0])
        ar=0
        for i in range(n):
            for j in range(m):
                matrix[i][j]=int(matrix[i][j])
                if i!=0:
                    if matrix[i][j]!=0:
                        matrix[i][j]+=matrix[i-1][j]
            ar=max(ar,func(matrix[i]))
        return ar
        
                    