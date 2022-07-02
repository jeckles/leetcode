class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans, i, finished = 0, 0, False
        for container in boxTypes:
            while container[0] > 0:
                ans += container[1]
                container[0] -= 1
                truckSize -= 1
                if truckSize == 0:
                    finished = True
                    break
            if finished: 
                break
        return ans
