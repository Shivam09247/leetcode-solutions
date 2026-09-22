class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        dic = {}
        ans = 0
        for num in nums:
            if num - k in dic:
                ans += dic[num - k]

            if num + k in dic:
                ans += dic[num + k]

            dic[num] = dic.get(num, 0) + 1

        return ans