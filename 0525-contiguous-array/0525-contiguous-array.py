class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: -1}
        prefix = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in dic:
                max_len = max(max_len, i - dic[prefix])
            else:
                dic[prefix] = i
        return max_len