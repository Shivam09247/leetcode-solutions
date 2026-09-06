class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a = True  
        b = True 

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                a = False

            if nums[i] < nums[i - 1]:
                b = False

        return a or b


        