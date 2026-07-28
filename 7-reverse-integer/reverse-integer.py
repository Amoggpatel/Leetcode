class Solution:
    def reverse(self, x: int) -> int:
        int_min = -2**31
        int_max = 2**31 -1

        sign = -1 if x < 0 else 1
        x = abs(x)

        reverse = 0

        while x != 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        reverse *= sign

        if reverse < int_min or reverse > int_max:
            return 0

        return reverse