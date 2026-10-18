# Quadratic Equation Roots

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a quadratic equation  **ax2 + bx + c = 0**, find its roots. If the equation has real roots, then return floor value of each root in decreasing order, If the roots are imaginary return  **-1**, the driver code will print  **Imaginary**.

 **Examples:** 

```
Input: a = 1, b = -2, c = 1
Output: [1, 1]
Explanation: Roots of equation x2-2x+1 are 1 and 1.
```

```
Input: a = 1, b = -7, c = 12
Output: [4, 3]
Explanation: Roots of equation x2 - 7x + 12 are 4 and 3.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-18T06:18:31.025Z  

```py
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
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/quadratic-equation-roots/1)