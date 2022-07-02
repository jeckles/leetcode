class Solution:  
    def compareBracket(self, leftBracket, rightBracket):
            if leftBracket == "{" and rightBracket == "}":
                return True    
            elif leftBracket == "(" and rightBracket == ")":
                return True
            elif leftBracket == "[" and rightBracket == "]":
                return True
            return False

    def isValid(self, s: str) -> bool:
        q, i, s = [], 0, list(s)
        while len(s) > 0:
            if s[0] == "(" or s[0] == "{" or s[0] == "[":
                q.append(s[0])
                s.pop(0)
            else:
                if len(q) > 0:
                    leftBracket = q[-1]
                else:
                    return False
                q.pop()
                if not(self.compareBracket(leftBracket, s[0])):
                    return False
                s.pop(0)
            i += 1
        if len(q) == 0 and len(s) == 0:
            return True
