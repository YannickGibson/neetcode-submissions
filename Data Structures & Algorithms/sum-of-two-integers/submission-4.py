class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            tmp = a ^ b
            b = (a & b) << 1
            a = tmp
            a &= mask
            b &= mask
        return a if a <= max_int else ~(a ^ mask);