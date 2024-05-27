# leetcode problem 91, number of Decodings

class Solution:
    def numDecodings(self, s: str) -> int:
        i, decodings = 0, [""]
        while i < len(s):
            j = i + 1
            if s[i] == "0":
                i += 1
            else:
                new_decodings = []
                if j < len(s):
                    for d in decodings:
                        new_decodings.add(d + str(chr(int(s[i]))))
                        new_decodings.add(d + str(chr(int(s[i:j])))
                else:
                    new_decodings.add(d + str(chr(int(s[i]))))
            i += 1       
        return decodings


sol = Solution()