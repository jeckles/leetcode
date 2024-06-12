class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans, char_set, wordshs = [], set(list("".join(words))), {}
        for word in words:
            wordshs[word] = {}
            chars = list(word)
            for c in chars:
                if c not in wordshs[word].keys():
                    wordshs[word][c] = 1
                else:
                    wordshs[word][c] += 1
        
        print(chars)
        print(wordshs)

        for c in char_set:
            occ = float('inf')
            for word in wordshs:
                if c in wordshs[word]:
                    occ = min(occ, wordshs[word][c])
                else:
                    occ = float('inf')
                    break
            if occ != float('inf'):
                for i in range(occ):
                    ans.append(c)
        return ans

sol, words = Solution(), ["woord", "wooordle", "poodlle"]
print(sol.commonChars(words))
