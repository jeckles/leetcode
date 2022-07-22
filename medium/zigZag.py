class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        letters, currLetter, totalLetter, board, i, finished, ans = list(s), 0, len(s), [[] for i in range(numRows)], 0, False, []
        board[i].append(letters[currLetter])
        while i < numRows - 1 and currLetter < totalLetter - 1:
            i += 1
            currLetter += 1
            board[i].append(letters[currLetter])
            if currLetter == totalLetter - 1:
                break
            if i == numRows - 1: # here we want to start going back up...
                while i > 0 and currLetter < totalLetter - 1:
                    i -= 1
                    currLetter += 1
                    if currLetter == totalLetter:
                        finished = True
                        break
                    board[i].append(letters[currLetter])
                    if i == 0:
                        break
            if finished:
                break
        
        for row in board:
            ans += row
        return "".join(char for char in ans)
