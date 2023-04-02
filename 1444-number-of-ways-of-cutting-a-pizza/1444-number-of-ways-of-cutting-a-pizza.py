class Solution:
    
    def helper(self,li,i,j,k,dp):
        # print('efef',i,j,k)
        if k==1 and li[i][j]>0:return 1
        if li[i][j]<k: return  0
        
        
        op=0
        
        for row in range(i+1,len(li)):
            if li[i][j]-li[row][j]>0: 
                # print(row,j,k-1)
                # print(dp)
                if dp[row][j][k-1]==-1:dp[row][j][k-1]=self.helper(li,row,j,k-1,dp)
                op+=dp[row][j][k-1]
        for col in range(j+1,len(li[0])):
            if li[i][j]-li[i][col]>0:
                if dp[i][col][k-1]==-1:dp[i][col][k-1]=self.helper(li,i,col,k-1,dp)
                op+=dp[i][col][k-1]
        return op
        
        
        
    def ways(self, arr: List[str], k: int) -> int:
        
        dp=[[[-1 for i in range(k+1)] for i in range(len(arr[0]))] for i in range(len(arr))]
        # for ele in dp:
        #     print(ele)
        li=[[0 for i in range(len(arr[0]))]for i in range(len(arr))]
        for i in range(len(arr)-1,-1,-1):
            for j in range(len(arr[0])-1,-1,-1):
                z=-1
                if i==len(arr)-1:
                    x=0
                    z=0
                else:
                    x=li[i+1][j]
                if j==len(arr[0])-1:
                    y=0
                    z=0
                else:
                    y=li[i][j+1]
                if z==-1:
                    z=li[i+1][j+1]
                if arr[i][j]=='.':
                    li[i][j]=x+y-z
                else: 
                    li[i][j]=1+x+y-z
        # print(k)
        return self.helper(li,0,0,k,dp)%(1000000007)