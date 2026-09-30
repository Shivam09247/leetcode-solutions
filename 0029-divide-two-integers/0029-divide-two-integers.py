class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            current = divisor
            multiple = 1

            while current + current <= dividend:
                current += current
                multiple += multiple

            dividend -= current
            quotient += multiple

        return -quotient if negative else quotient