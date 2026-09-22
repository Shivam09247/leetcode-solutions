class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        dic = {}
        good = 0
        for i, num in enumerate(nums):
            key = num - i
            if key in dic:
                good += dic[key]
            dic[key] = dic.get(key, 0) + 1
        total = len(nums) * (len(nums) - 1) // 2
        return total - good