class Solution(object):
    def binSearch(self,nums,target):
        low , high = 0 , len(nums)-1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid]<target:
                low = mid + 1
            elif nums[mid]>target:
                high = mid - 1
            else:
                return True
        return False
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix[0])
        for row in matrix:
            if row[0]>target:
                return False
            else:
                if self.binSearch(row,target):
                    return True
        return False

        
        

        