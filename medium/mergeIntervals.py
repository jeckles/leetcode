class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals, ans, i = sorted(intervals, key=lambda x:x[1]), [], 0

        while i < len(intervals):
            j = i + 1
            while j < len(intervals):
                print("intervals[i] is {0} intervals[j] is {1}".format(intervals[i], intervals[j]))
                if (not(intervals[j][0] <= intervals[i][1] and intervals[j][0] >= intervals[i][0])):
                    break
                else:
                    print('here')
                    intervals[i][1] = intervals[j][1] # extend the outer range
                    j += 1
            ans.append(intervals[i])
            i = j

        return ans

sol, intervals = Solution(), [[2, 4], [1, 3], [5, 10]]
print(sol.merge(intervals))