# Count Perfect Squares

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a positive integer  **n**, find the number of perfect squares that are less than  **n**  in the sample space of perfect squares. The sample space consists of all perfect squares starting from 1 (i.e., 1, 4, 9, 16, 25, …)

 **Examples :** 

```
Input: n = 9
Output: 2
Explanation: 1 and 4 are the only Perfect Squares less than 9. So, the Output is 2.
```

```
Input: n = 3
Output: 1
Explanation: 1 is the only Perfect Square less than 3. So, the Output is 1.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T06:50:35.719Z  

```py
import math
class Solution:
    def countSquares(self, n):
        # code here 
        if n > 1:
            count = math.isqrt(n-1)
                
        return count
                
            
            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-squares3649/1)