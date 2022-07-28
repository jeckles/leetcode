'''
[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]]
"SEE"

[["a","b"],
 ["c","d"]]
"abcd"

[["A","B","C","E"],
 ["S","F","E","S"],
 ["A","D","E","E"]]
"ABCESEEEFS"
'''

from typing import List, Optional

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        i, j, word = 0, 0, list(word)
        while i < len(board):
            j = 0
            while j < len(board[0]):
                if board[i][j] == word[0]:
                    visited, wordCopy = [], word.copy()
                    check = self.explore(board, i, j, visited, wordCopy)
                    if check:
                        return True
                j += 1
            i += 1
        return False

    def explore(self, board, i, j, visited, word):
        if i < len(board) and i > -1 and j < len(board[0]) and j > -1:
            if (i, j) not in visited:
                if board[i][j] == word[0]:
                    if len(word) == 1: # at this point you have found the last character of the word...
                        return True
                    else:
                        word.pop(0)
                        cVisited = visited.copy()
                        cVisited.append((i, j))
                        left = self.explore(board, i, j - 1, cVisited, word.copy())
                        right = self.explore(board, i, j + 1, cVisited, word.copy())
                        up = self.explore(board, i - 1, j, cVisited, word.copy())
                        down = self.explore(board, i + 1, j, cVisited, word.copy())
                        if left or right or up or down:
                            return True
                else:
                    return False
            else:
                return False
        else:
            return False

def main():
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'E', 'S'], ['A', 'D', 'E', 'E']]
    sol = Solution()
    print(sol.exist(board, "ABCESEEEFS"))

if __name__ == "__main__":
    main()
