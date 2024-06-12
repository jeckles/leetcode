# after placing parenthesis, you can close it, or continue placing open
# ( goes down, two options. close with ), subtrack your number of parenthesis
# or continue with another open, (. when you eventually do close, you want to decrease your num.
# when you get to 0, then you want to add your string to your answers.
# you cannot place two right parenthesis in a row.
# how do you know not to place a closed parenthesis... 
# keep a stack, and peek at the last placed ?
# and then pop when you get to a closed parenthesis

class Solution(object):
    def buildString(self, n, s, ss):
        results = []
        if n == 0:
            return ["".join(s)]
        
        if len(ss) > 0:
            res = self.buildString(n - 1, s[:].append('('), ss[:].append('('))
            results.extend(res)
        else:
            ss = ss[:-1]
            res = self.buildString(n, s[:].append(')'), ss)
            results.extend(res)
            
        return results

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.buildString(n, ['('], ['('])
    
sol, n = Solution(), 3
print(sol.generateParenthesis(n))