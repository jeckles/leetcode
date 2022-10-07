from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, minBound, maxBound = 0, len(height) - 1, 0, len(height) - 1
        while i < j:
            

def main():
    sol = Solution()
    heights = [5, 1, 4, 5]
    sol.maxArea(heights)

if __name__ == "__main__":
    main()
