class Solution(object):
    def colorIsland(self, i, j, grid, numIslands):
        if i < len(grid) and i >= 0 and j < len(grid[i]) and j >= 0 and grid[i][j] != str(0) and grid[i][j] != str(numIslands):
            grid[i][j] = str(numIslands)
            self.colorIsland(i + 1, j, grid, numIslands)
            self.colorIsland(i - 1, j, grid, numIslands)
            self.colorIsland(i, j + 1, grid, numIslands)
<<<<<<< HEAD
            self.colorIsland(i, j - 1, grid, numIslands)    
=======
            self.colorIsland(i, j - 1, grid, numIslands) 
>>>>>>> 8a0bb27f02ff6bd30642c4d1ed537c8dd69e2749
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
<<<<<<< HEAD
        numIslands -= 1
        return numIslands
    
=======
            numIslands -= 1
            return numIslands

>>>>>>> 8a0bb27f02ff6bd30642c4d1ed537c8dd69e2749
s, grid = Solution(), [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]
print(s.numIslands(grid))