class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            i, j, ans, index = 0, 1, "", float('inf')
            while j < len(strs):
                strArr1, strArr2, k = list(strs[i]), list(strs[j]), 0
                while k < len(strArr1) and k < len(strArr2) and strArr1[k] == strArr2[k]:
                    k += 1
                index = min(index, k)
                ans = strArr1[0:index]
                j += 1
        return "".join(char for char in ans)
