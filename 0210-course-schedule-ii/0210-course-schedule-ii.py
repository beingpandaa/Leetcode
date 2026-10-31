class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visited = set()
        completed = set()
        op = []
        def dfs(crs):
                if crs in visited: return False
                if crs in completed:return True
                visited.add(crs)

                for pre in preMap[crs]:
                    if not dfs(pre): return False
                visited.remove(crs)
                completed.add(crs)
                op.append(crs)
                return True
        for crs in range(numCourses):
            if not dfs(crs):return []
        return op