class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        i, j, phone = 0, 0, {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        combo, sol, letterIndex = "", [], 0
        self.generateCombinations(letterIndex, combo, sol, phone, digits)
        return sol
        
    def generateCombinations(self, letterIndex, combo, sol, phone, digits):
        currCombo = combo
        if letterIndex < len(digits):
            currDigit, i = int(digits[letterIndex]), 0
            while i < len(phone[currDigit]):
                currCombo += phone[currDigit][i]
                if len(currCombo) == len(digits):
                    sol.append(currCombo)
                else:
                    self.generateCombinations(letterIndex + 1, currCombo, sol, phone, digits)
                i += 1
                currCombo = combo
        return
