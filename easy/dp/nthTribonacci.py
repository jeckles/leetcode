class Solution:
    def nthTribonacci(self, n):
        i, cache = 3, [0, 1, 1]
        while i <= n:
            cache.append(self.__nthTribonacci(i - 1, cache) + self.__nthTribonacci(i - 2, cache) + self.__nthTribonacci(i - 3, cache))
            i += 1
        return cache[n]

    def __nthTribonacci(self, i, cache):
        if i < 0:
            return 0
        else:
            return cache[i]

def main():
    solution = Solution()
    print(solution.nthTribonacci(6))

if __name__ == "__main__":
    main()
