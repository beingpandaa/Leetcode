class Solution:
    def checkSlope(self,x1,x2,y1,y2):
        if x1==x2:return sys.maxsize
        return ((y1-y2)/(x1-x2))
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope=self.checkSlope(coordinates[0][0],coordinates[1][0],coordinates[0][1],coordinates[1][1])
        for coordinate in coordinates[2:]:
            x,y=coordinate
            if self.checkSlope(x,coordinates[0][0],y,coordinates[0][1])!=slope:return False
        return True
            