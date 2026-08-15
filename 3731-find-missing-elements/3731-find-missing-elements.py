class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ma=float("-inf")
        mi=float("inf")
        s=set()
        for i in nums:
            if i>ma:
                ma=i
            if i<mi:
                mi=i
            s.add(i)
        lst=[]
        for i in range(mi+1,ma):
            if i not in s:
                lst.append(i)
        return lst
        