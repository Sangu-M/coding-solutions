# sum-of-ap-series4512

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T16:17:45.328Z  

```py
class Solution:
    def sumOfAP(self, n, a, d):
        # code here
        result = 0
        s = 0
        for i in range(0,n):
            result = a + (i*d)
            s+=result
        return s
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sum-of-ap-series4512/1)