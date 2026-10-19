class Solution:
    def sumOfSeries(self,n):
        #code here
        result = 0
        for i in range(n+1):
            result = result + (i**3)
            
        return result