class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        lst=[[],[]]
        s1=set()
        s2=set()
        for i in nums1:
            s1.add(i)
        for i in nums2:
            s2.add(i)
        for i in s1:
            if i not in s2:
                lst[0].append(i)
        for i in s2:
            if i not in s1:
                lst[1].append(i)
        return lst
        