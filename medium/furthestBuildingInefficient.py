class Solution(object):
    
    def furthestBuildingHelper(self, index, heights, bricks, ladders):
        
        # made it to the end of the heights list 
        if index == len(heights) - 1:
            return 0
        
        # not enough bricks and out of ladders
        if bricks < heights[index + 1] - heights[index] and ladders == 0:
            return 0
        
        # here we just move forward
        if heights[index + 1] <= heights[index]:
            return 1 + self.furthestBuildingHelper(index + 1, heights, bricks, ladders)
        
        # we do have enough bricks
        elif heights[index + 1] > heights[index]:
            diff = heights[index + 1] - heights[index]
            # we have two routes we can take, one using ladders and the other using bricks
            # must check if we have ladders to use
            if bricks >= diff:
                if ladders > 0:
                    laddersRoute = self.furthestBuildingHelper(index + 1, heights, bricks, ladders - 1)
                    bricksRoute = self.furthestBuildingHelper(index + 1, heights, bricks - diff, ladders)
                    return 1 + max(laddersRoute, bricksRoute)
                else:
                    return 1 + self.furthestBuildingHelper(index + 1, heights, bricks - diff, ladders)
            else:
                if ladders > 0:
                    return 1 + self.furthestBuildingHelper(index + 1, heights, bricks, ladders - 1)
                else:
                    return 0
            
    
    def furthestBuilding(self, heights, bricks, ladders):
        
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        
        furthest = self.furthestBuildingHelper(0, heights, bricks, ladders)
        return furthest
        
