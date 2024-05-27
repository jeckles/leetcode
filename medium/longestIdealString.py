# brute force, double for loop for each character

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        s, substrings = list(s), list(s[0])
        for i in range(1, len(s)):
            updated, toAdd = False, []
            for index, substring in enumerate(substrings):
                if abs(ord(s[i]) - ord(substring[-1])) <= k: # if this condition is met, add s to the end of each substring   
                    toAdd.append(substrings[index] + str(s[i]))  
                    updated = True
            substrings += toAdd
            if not(updated):                    
                substrings.append(s[i]) # is this condition is not met, add s as a new entry into the list of subStrings
        maxLen = -1
        for substring in substrings:
            if len(substring) > maxLen:
                maxLen = len(substring)    
        return maxLen
    
sol, s, k = Solution(), "dyyonfvzsretqxucmavxegvlnnjubqnwrhwikmnnrpzdovjxqdsatwzpdjdsneyqvtvorlwbkb", 7

print(sol.longestIdealString(s, k))