class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        ans = -1

        for i in s:
            if i > 0 and -i in s:
                ans = max(ans, i)

        return ans