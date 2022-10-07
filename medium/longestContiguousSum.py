class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, currSum, maxSum = 0, 0, -float('inf')
        while i < len(nums):
            if nums[i] > currSum + nums[i]:
                currSum = nums[i]
            else:
                currSum += nums[i]
            maxSum = max(maxSum, currSum)
            i += 1
        return maxSum
