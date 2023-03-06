class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li=[]
        for row in range(1,numRows+1):
            temp=[]
            for i in range(row):
                if i==0 or i==row-1:temp.append(1)
                else:temp.append(li[row-2][i]+li[row-2][i-1])
            li.append(temp)
        return li
        