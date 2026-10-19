class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        n=len(arr)
        
        if n%2 !=0:
            mid = n//2
            return arr[mid]
        else:
            mid = n//2
            return (arr[mid-1]+arr[mid])/2