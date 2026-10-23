# Sum of AP series

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

A series with same common difference is known as arithmetic series. The first term of series is ' **a** ' and common difference is  **d**. The series looks like a, a + d, a + 2d, a + 3d,... Find the sum of series upto  **nth**  term.

 **Examples :** 

```
Input: n = 5, a = 1, d = 3
Output: 35
Explanation: Series upto 5th term is 1 4 7 10 13, so sum will be 35.

```

```
Input: n = 3, a = 1, d = 2
Output: 9
Explanation: Series upto 3rd term is 1 3 5, so sum will be 9.

```

 **Constraints:** 
1 ≤ n ≤ 500
0 ≤ a, d ≤ 500

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T16:14:30.584Z  

```py
class Solution:
    def sumOfAP(self, n, a, d):
        # code here
        result = 0
        s = []
        for i in range(0,n):
            result = a + (i*d)
            s.append(result)
        return sum(s)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sum-of-ap-series4512/1)