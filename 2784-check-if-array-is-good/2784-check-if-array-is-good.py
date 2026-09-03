class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False
        dic = {}
        for x in nums:
            dic[x] = dic.get(x, 0) + 1
        for i in range(1, n):
            if dic.get(i, 0) != 1:
                return False
        return dic.get(n, 0) == 2