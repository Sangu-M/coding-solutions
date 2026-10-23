# GCD of Two

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two positive integers  **a**  and  **b**, find  **GCD** of a and b.

 **Note:**  Don't use the inbuilt gcd function

 **Examples:** 

```
Input: a = 20, b = 28
Output: 4
Explanation: GCD of 20 and 28 is 4
```

```
Input: a = 60, b = 36
Output: 12
Explanation: GCD of 60 and 36 is 12
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T03:35:47.431Z  

```py
class Solution:
    def gcd(self, a, b):
        while b!=0:
            reminder = a%b
            a=b
            b= reminder
        return a
                
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1)