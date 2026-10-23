# Replace all 0's with 5

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

You are given an integer  **n**. You need to convert all zeroes of  **n**  to 5.

 **Examples:** 

```
Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.

```

```
Input: n = 121
Output: 121
Explanation: Since there are no zeroes in 121, the number remains as 121.
```

 **Constraints:** 
0 <= n <= 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T16:26:38.986Z  

```py
class Solution:
    def convertFive(self, n):
        # code here
        s = str(n)
        s1=s.replace("0","5")
        n1 = int(s1)
        return n1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/replace-all-0s-with-5/1)