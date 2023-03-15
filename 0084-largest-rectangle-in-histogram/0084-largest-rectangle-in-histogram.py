class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
#         ans=0
#         i=0
#         while i<len(heights):
        
            
#             low=i-1
#             high=i
#             while low>-1 and heights[low]>=heights[i]:
#                 low-=1
#             while high+1<len(heights) and heights[high+1]>=heights[i]:
#                 high+=1
            
#             total=((i-low)+(high-i))*heights[i]
#             # print("I am at i: ",i," with low,high: ",low,high," and total: ",total )
#             ans=max(ans,total)
#             while i+1<len(heights) and heights[i+1]==heights[i]:
#                 i+=1
#             i+=1
#         return ans
        stack=[]
        index=0
        maxArea=0
        ele=(heights[index],index)
        while index<len(heights):
            # print(stack,maxArea)
            start=index
            while stack and stack[-1][0]>heights[index]:
                h,i=stack.pop()
                maxArea=max(maxArea,(index-i)*h)
                start=i
            stack.append((heights[index],start))
            index+=1
            
        while stack:
            u=stack.pop()
            maxArea=max(maxArea,(len(heights)-u[1])*u[0])
        return maxArea
                
                
            
            
        