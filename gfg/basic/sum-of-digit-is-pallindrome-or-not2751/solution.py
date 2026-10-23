class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        s = str(n)
        l = list(s)
        result = 0
        for i in l:
            result=result+int(i)
        s1 = str(result)
        l1 = list(s1)
        l1.reverse()
        l2 = "".join(l1)
        l3 = int(l2)
        if l3 == result:
            return True
        else:
            return False