from typing import List
from heapq import heappush
from heapq import heappop
'''

[10, 9, 2, 5, 3, 7, 101, 18]

- use a min heap to keep track of values already visited
- when visiting a value, we want to pull the smallest value off the min heap that is greater than our value
- once we have this value, we want to use the number of values greater than it to get our sum for that index
- if we have no value in our minHeap that is greater than the value we are looking at, then we just enter 0 for the
  index we are currently looking at

18 -> 1

101 -> look at 18, it is less, avoid -> 1

7 -> look at 18, it is more, use it -> 2

3 -> look at 7, it is more, use it -> 3

5 -> look at 3, it is less, avoid -> look at 7, it is more, use it -> 3

2 -> look at 3, it is more, use it -> 4

9 -> look at 2, it is less, avoid it -> look at 3, less, avoid -> look at 5 less, avoid -> 7, less, avoid -> 18, more,
use -> 1

10 -> look at 2, it is less, avoid it -> look at 3, less, avoid -> look at 5, less, avoid -> 7, less, avoid -> 9, less,
avoid, 18, more, use it -> 2

4 is the max, return it

avoid

'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        i, minHeap = len(nums) - 2, []
        heappush(minHeap, (nums[len(nums) - 1], 1))
        while i >= 0:
            addBack, smallest = [], heappop(minHeap)
            addBack.append(smallest)
            num, value = smallest
            while num < nums[i] and len(minHeap) > 0:
                smallest = heappop(minHeap)
                addBack.append(smallest)
            num, value = smallest
            if num > nums[i]:    
                heappush(minHeap, (nums[i], value + 1))
            else:
                heappush(minHeap, (nums[i], 1))
            for toAdd in addBack:
                heappush(minHeap, toAdd)
            i -= 1
        maxVal = -1
        while len(minHeap) > 0:
            num, val = heappop(minHeap)
            maxVal = max(val, maxVal)
        return maxVal

def main():
    nums, sol = [10,9,2,5,3,7,101,18], Solution()
    print("*********INPUT**********")
    print(nums)
    print("*********OUTPUT*********")
    print(sol.lengthOfLIS(nums))

if __name__ == "__main__":
    main()
