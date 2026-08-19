class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ma=float("-inf")
        for i in candies:
            if i>ma:
                ma=i
        for i in range(len(candies)):
            if candies[i]+extraCandies >= ma:
                candies[i]=True
            else:
                candies[i]=False
        return candies
        