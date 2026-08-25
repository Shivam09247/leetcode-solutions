class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ma1 = float("-inf")
        ma2 = float("-inf")
        ma3 = float("-inf")

        for i in nums:
            if i == ma1 or i == ma2 or i == ma3:
                continue

            if i > ma1:
                ma3 = ma2
                ma2 = ma1
                ma1 = i
            elif i > ma2:
                ma3 = ma2
                ma2 = i
            elif i > ma3:
                ma3 = i

        if ma3 == float("-inf"):
            return ma1

        return ma3