class Solution:
    def fourSumCount(
        self,
        nums1: list[int],
        nums2: list[int],
        nums3: list[int],
        nums4: list[int]
    ) -> int:
        pair_sum = {}
        for a in nums1:
            for b in nums2:
                total = a + b
                pair_sum[total] = pair_sum.get(total, 0) + 1
        count = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                count += pair_sum.get(target, 0)

        return count