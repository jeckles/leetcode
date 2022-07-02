class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j, leftBorder, rightBorder, topBorder, bottomBorder = 0, 0, 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        result, length, finished = [matrix[i][j]], len(matrix) * len(matrix[0]), False
        
        while len(result) != length:
                while j < rightBorder:
                    j += 1
                    result.append(matrix[i][j])
                    if length == len(result):
                        finished = True
                topBorder += 1

                if finished:
                    break                
                while i < bottomBorder:
                    i += 1
                    result.append(matrix[i][j])
                    if length == len(result):
                        finished = True
                rightBorder -= 1

                if finished:
                    break
                while j > leftBorder:
                    j -= 1
                    result.append(matrix[i][j])
                    if length == len(result):
                        finished = True
                bottomBorder -= 1

                if finished:
                    break
                while i > topBorder:
                    i -= 1
                    result.append(matrix[i][j])
                    if length == len(result):
                        finished = True
                leftBorder += 1  
                
        return result
