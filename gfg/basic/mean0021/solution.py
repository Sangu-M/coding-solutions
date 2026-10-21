class Solution:
    def findMean(self, arr):
        # code here 
        s = sum(arr)
        s1 = s//len(arr)
        return s1