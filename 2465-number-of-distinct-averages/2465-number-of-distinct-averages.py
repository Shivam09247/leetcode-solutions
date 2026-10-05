class Solution:
    def distinctAverages(self, nums):
        nums.sort()
        dic = {}
        i = 0
        j = len(nums) - 1

        while i < j:
            avg = (nums[i] + nums[j]) / 2
            dic[avg] = 1

            i += 1
            j -= 1

        return len(dic)