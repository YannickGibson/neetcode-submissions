class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFF
        while b & mask != 0:
            tmp = a ^ b
            b = (a & b) << 1
            a = tmp
        if b <= 0:  # if a is negative, keep its infinite 1111's
            return a
        else:  # else truncate the overflow
            return a & mask