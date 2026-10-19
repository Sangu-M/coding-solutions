class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        
        
        if len(arr)%2 !=0:
            mid = len(arr)//2
            return arr[mid]
        else:
            mid = len(arr)//2
            return (arr[mid-1]+arr[mid])/2