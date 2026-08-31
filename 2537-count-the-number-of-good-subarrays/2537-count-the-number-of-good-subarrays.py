class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        dic = {}
        left = 0
        pairs = 0
        ans = 0
        for right in range(len(nums)):
            x = nums[right]
            pairs += dic.get(x, 0)
            dic[x] = dic.get(x, 0) + 1
            while pairs >= k:
                ans += len(nums) - right
                x = nums[left]
                dic[x] -= 1
                pairs -= dic[x]
                left += 1

        return ans
