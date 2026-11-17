class Solution:
    def reverse(self, x: int) -> int:
        def rec(n: int, rev: int) -> int:
            if n == 0:
                return rev

            rev = rev * 10 + n % 10
            return rec(n // 10, rev)

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = rec(x, 0)
        reversed_num *= sign
        if reversed_num < -(1 << 31) or reversed_num > (1 << 31) - 1:
            return 0

        return reversed_num

# Brute Force - 
# class Solution:
#     def reverse(self, x: int) -> int:
#         org = x
#         x = abs(x)
#         res = int(str(x)[::-1])
#         if org < 0:
#             res *= -1
#         if res < -(1 << 31) or res > (1 << 31) - 1:
#             return 0
#         return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna