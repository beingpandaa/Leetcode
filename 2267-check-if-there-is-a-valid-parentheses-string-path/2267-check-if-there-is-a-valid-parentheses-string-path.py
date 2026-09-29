class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 == 1:return False

        @cache
        def dfs(i, j, balance):
            if i >= m or j >= n:return False
            if grid[i][j] == '(':balance += 1
            else:balance -= 1
            if balance < 0:return False
            remaining = (m - 1 - i) + (n - 1 - j)
            if balance > remaining:return False
            if i == m - 1 and j == n - 1:return balance == 0
            return dfs(i + 1, j, balance) or dfs(i, j + 1, balance)
            
        return dfs(0, 0, 0)