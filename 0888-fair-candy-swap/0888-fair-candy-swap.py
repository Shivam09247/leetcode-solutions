class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        A = sum(aliceSizes)
        B = sum(bobSizes)
        diff = (B - A) // 2
        bob = set(bobSizes)
        for a in aliceSizes:
            b = a + diff
            if b in bob:
                return [a, b]