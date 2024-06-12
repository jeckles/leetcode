class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j, s = 0, len(s) - 1, list(s)
        while j > i:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -= 1
            i += 1
        return "".join(s)

sol, s = Solution(), "hello"
print(sol.reverseString(s))