class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)

        count = {}

        for i, num in enumerate(sorted_nums):
            if num not in count:
                count[num] = i

        return [count[num] for num in nums]