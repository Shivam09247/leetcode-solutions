class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        ans = 0
        for num in nums:
            if num in dic:
                ans += dic[num]

            dic[num] = dic.get(num, 0) + 1

        return ans