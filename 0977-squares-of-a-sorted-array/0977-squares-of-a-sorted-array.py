class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                answer[i] = nums[left] ** 2
                left += 1
            else:
                answer[i] = nums[right] ** 2
                right -= 1

        return answer