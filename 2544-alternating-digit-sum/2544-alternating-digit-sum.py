class Solution:
    def alternateDigitSum(self, n: int) -> int:
        r = 0
        m = list(str(n))

        for i in range(len(m)):
            if i % 2 == 0:
                r += int(m[i])
            else:
                r -= int(m[i])

        return r