class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        ma1=float("inf")
        ma2=float("inf")
        for i in prices:
            if i<ma2:
                ma2=i
            if ma2<ma1:
                a=ma1
                ma1=ma2
                ma2=a
        if money-(ma1+ma2)>=0:
            return money-(ma1+ma2)
        return money
                
        