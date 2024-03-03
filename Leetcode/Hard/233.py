class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count = 0
        factor = 1

        while n // factor != 0:
            current_digit = (n // factor) % 10
            before = n // (factor * 10)
            after = n % factor

            if current_digit == 0:
                count += before * factor
            elif current_digit == 1:
                count += before * factor + after + 1
            else:
                count += (before + 1) * factor

            factor *= 10

        return count