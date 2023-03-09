class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r=0,len(matrix)-1
        while l<r:   #the outer while loop is for interating from outer to inner squares
            for i in range(r-l):   #the inner for loop is for shifting the the vizualized square in the present outer square 
                top,bottom=l,r
                topleft=matrix[top][l+i]
                matrix[top][l+i]=matrix[bottom-i][l]
                matrix[bottom-i][l]=matrix[bottom][r-i]
                matrix[bottom][r-i]=matrix[top+i][r]
                matrix[top+i][r]=topleft
            
            l+=1
            r-=1
            