class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        import heapq
        for i in nums:
            dic[i]=dic.get(i,0)+1
        heap=[]
        for i,j in dic.items():
            heapq.heappush(heap,(j,i))
            if len(heap)>k:
                heapq.heappop(heap)
        return [i[1] for i in heap]


