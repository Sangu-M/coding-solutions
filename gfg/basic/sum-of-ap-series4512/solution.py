class Solution:
    def sumOfAP(self, n, a, d):
        # code here
        result = 0
        s = []
        for i in range(0,n):
            result = a + (i*d)
            s.append(result)
        return sum(s)