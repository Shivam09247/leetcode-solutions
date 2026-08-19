class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        dic={0:0}
        s=0
        for i in range(len(gain)):
            s+=gain[i]
            dic[i+1]=s
        ma=float('-inf')
        for i in dic:
            if dic[i]>ma:
                ma=dic[i]
        return ma        