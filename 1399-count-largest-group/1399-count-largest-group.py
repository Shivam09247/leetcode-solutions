class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}

        for i in range(1, n + 1):
            digit_sum = sum(map(int, str(i)))
            dic[digit_sum] = dic.get(digit_sum, 0) + 1

        max_size = max(dic.values())

        return sum(1 for size in dic.values() if size == max_size)