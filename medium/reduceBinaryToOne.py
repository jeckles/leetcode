class Solution(object):
    def getNumber(self, s):
        s, num = list(s), 0
        for i in range(len(s)):
            num += (2 ** i) * int(s[i])
        return num
            
    def numSteps(self, s):
        num, count = self.getNumber(s), 0
        while num != 1:
            if num % 2 == 1:
                num += 1
            else:
                num /= 2
            count += 1
        return count

s, binary = Solution(), "1101"

print(s.numSteps(binary))
