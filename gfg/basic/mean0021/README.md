# Mean or Average of Array

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an array  **arr[]**, return the floor value of the mean of its elements.

 **Examples:** 

```
Input: arr[] = [1, 3, 4, 2, 6, 5, 8, 7]
Output: 4
Explanation: Sum of the elements is 1 + 3 + 4 + 2 + 6 + 5 + 8 + 7 = 36, Mean = 36/8 = 4.5, floor(4.5) = 4.
```

```
Input: arr[] = [4, 4, 4, 4, 4]
Output: 4
Explanation: Sum of the elements is 4 + 4 + 4 + 4 + 4 = 20, Mean = 20/5 = 4
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T07:59:36.630Z  

```py
class Solution:
    def findMean(self, arr):
        # code here 
        s = sum(arr)
        s1 = s//len(arr)
        return s1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/mean0021/1)