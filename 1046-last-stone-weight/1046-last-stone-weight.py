class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap=[]
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>1:
            a=-(heapq.heappop(heap))
            b=-(heapq.heappop(heap))
            if a==b:
                heap=heap
            else:
                c=abs(a-b)
                heapq.heappush(heap,-c)
        return -heap[0] if len(heap)>0  else 0
        