class Solution:
    def maxProduct(self, n: int) -> int:
        a = b = -1
        while n > 0:
            num = n % 10
            n //= 10

            if num > a:
                b = a
                a = num
            elif num > b:
                b = num

        return a * b
        