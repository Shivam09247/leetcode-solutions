class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ma=float("-inf")
        for i in accounts:
            s=0
            for j in i:
                s+=j
            if s>ma:
                ma=s
        return ma
        