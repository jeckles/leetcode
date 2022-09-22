class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s, answer = 0, []
        for num in nums:
            if num % 2 == 0:
                s += num
        for query in queries:
            val, index = query
            prevVal = nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                if prevVal % 2 != 0:
                    s += nums[index]
                else:
                    s -= prevVal
                    s += nums[index]
            else:
                s -= prevVal
            answer.append(s)
        return answer
