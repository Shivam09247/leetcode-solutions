class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        l=0
        for i in hours:
            if i>=target:
                l+=1
        return l