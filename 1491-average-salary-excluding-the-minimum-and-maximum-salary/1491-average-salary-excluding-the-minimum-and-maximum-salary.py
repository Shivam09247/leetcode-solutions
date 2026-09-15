class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        minimum = float("inf")
        maximum = float("-inf")
        for s in salary:
            total += s
            minimum = min(minimum, s)
            maximum = max(maximum, s)

        return (total - minimum - maximum) / (len(salary) - 2)