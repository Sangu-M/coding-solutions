import math
class Solution:
    l1 = list()
    def quadraticRoots(self, a, b, c):
        # code here
        d= (b**2) - (4*a*c)
        
        if d<0:
            return [-1]
            
        val1 = (-b + math.sqrt(d))/(2*a)
        val2 = (-b - math.sqrt(d))/(2*a)
        
        val3 = math.floor(val1)
        val4 = math.floor(val2)
        
        return [val3,val4]
        