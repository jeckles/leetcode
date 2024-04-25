# brute force, double for loop for each character

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        s = s.split()
        i, j, longest = 0, 1, -1
        while i < (len(s) - 1):
            while j < len(s):
                if ord()