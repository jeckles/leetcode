# naive, O(N^3) Solution. Wrong, does not account for all possible subsequences based on unique indices...
# recursion is needed to explore all paths
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subseqs = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                ss, diff = [nums[i], nums[j]], nums[j] - nums[i]
                print("nums[i] is {0}, nums[i + 1] is {1}, diff is {2}".format(nums[i], nums[i + 1], diff))
                for k in range(j + 1, len(nums)):
                    if (nums[k] - ss[-1]) == diff:
                        subseqs.append(ss + [nums[k]])
                        ss.append(nums[k])
        return subseqs

sol, nums = Solution(), [7, 7, 7, 7, 7]
print(sol.numberOfArithmeticSlices(nums))

# can we do better ? I believe we can

class Solution2(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pass
