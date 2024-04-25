class Solution(object):
    def colorIsland(self, i, j, grid, numIslands):
        if i < len(grid) and i >= 0 and j < len(grid[i]) and j >= 0 and grid[i][j] != str(0) and grid[i][j] != str(numIslands):
            grid[i][j] = str(numIslands)
            self.colorIsland(i + 1, j, grid, numIslands)
            self.colorIsland(i - 1, j, grid, numIslands)
            self.colorIsland(i, j + 1, grid, numIslands)
            self.colorIsland(i, j - 1, grid, numIslands)    
        return
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numIslands = 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    numIslands += 1
                    self.colorIsland(i, j, grid, numIslands)
        numIslands -= 1
        return numIslands
    
s, grid = Solution(), [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]
print(s.numIslands(grid))