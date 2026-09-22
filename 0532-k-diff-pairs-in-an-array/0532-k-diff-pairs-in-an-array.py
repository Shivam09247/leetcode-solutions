class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        ans = 0
        if k == 0:
            for num in dic:
                if dic[num] > 1:
                    ans += 1
        else:
            for num in dic:
                if num + k in dic:
                    ans += 1

        return ans