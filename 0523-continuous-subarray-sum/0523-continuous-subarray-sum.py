class Solution:
    def checkSubarraySum(self, nums, k):
        remainder = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            rem = prefix_sum % k

            if rem in remainder:
                if i - remainder[rem] >= 2:
                    return True
            else:
                remainder[rem] = i

        return False