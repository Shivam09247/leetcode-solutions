class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        c=set(nums3)
        d=a|b|c
        lst=[]
        for i in d:
            if (i in a and i in b) or (i in c and i in b) or (i in a and i in c):
                lst.append(i)
        return lst