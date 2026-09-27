import heapq
from math import isqrt

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        heap = [-x for x in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            remaining = isqrt(largest)

            heapq.heappush(heap, -remaining)

        return -sum(heap)