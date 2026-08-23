class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a=len(candyType)/2
        s=set()
        for i in candyType:
            s.add(i)
        return int(a) if a<len(s) else len(s)

        