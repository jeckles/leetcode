from typing import List, Optional

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words, i, result = {}, 0, []
        while i < len(strs):
            s = sorted(list(strs[i]))
            s = ''.join(s)
            if s in words.keys():
                words[s].append(i)
            else:
                words[s] = [i]
            i += 1
        for word in words.keys():
            agram = []
            for i in words[word]:
                agram.append(strs[i])
            result.append(agram)
        return result


def main():
    sol = Solution
    print(sol.groupAnagrams(["hello", "olleh", "this", "htis"]))
    
if __name__ == "__main__":
    main()
