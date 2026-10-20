class Solution:
    def closestNumber(self, n, m):
        # code here 
        q = n//m
        n1 = q*m
        n2 = (q + 1) * m
        
        d1 = abs(n-n1)
        d2 = abs(n-n2)
        
        if d1 < d2:
            return n1
        elif d2 < d1:
            return n2
        else:
            if abs(n1) > abs(n2):
                return n1
            else:
                return n2
        
            