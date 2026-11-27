class Solution:
    def numDecodings(self, s: str) -> int:
        


    # s = 111 -> (1, 11) (1, 1, 1), (11, 1)
        #   11
        #  i
        #  211
        # i
        # 3211

        # 123123
        #      11
        #     i
        #     21
        #    i
        #    32
        #   i
        #   33
        #  i
        #  63
        # i
        # 9


        one = 1 if s[-1] != "0" else 0
        two = 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] == "0":
                two = one
                one = 0
            elif int(s[i:i+2]) <= 26:
                tmp = two + one
                two = one
                one = tmp
            else:
                two = one
        return one