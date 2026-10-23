class Solution:
    def convertFive(self, n):
        # code here
        s = str(n)
        s1=s.replace("0","5")
        n1 = int(s1)
        return n1