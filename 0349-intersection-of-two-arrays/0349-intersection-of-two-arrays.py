class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set()
        lst=[]
        for i in nums1:
            if i not in s:
                s.add(i)
        for i in nums2:
            if i in s:
                lst.append(i)
                s.remove(i)
        return lst
        