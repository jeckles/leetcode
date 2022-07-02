class Solution(object):
    def rotate(self, matrix):
        rounds = len(matrix) / 2
        
        for i in range(rounds):
            iters, opp = len(matrix) - 2 * i - 1, len(matrix) - i - 1
            for j in range(iters):
                temp = matrix[i][i + j]
                matrix[i][i + j] = matrix[opp - j][i]
                matrix[opp - j][i] = matrix[opp][opp - j]
                matrix[opp][opp - j] = matrix[i + j][opp]
                matrix[i + j][opp] = temp
