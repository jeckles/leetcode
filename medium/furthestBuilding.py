import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        jumps_pq = []
	for i in range(len(heights) - 1):
	    height = heights[i + 1] - heights[i]
	    if height <= 0:
	        continue
	    heapq.heappush(jumps_pq, height)
	    if len(jumps_pq) > ladders:
	        bricks -= heapq.heappop(jumps_pq)
	    if bricks < 0:
	        return i

	return len(heights) - 1
