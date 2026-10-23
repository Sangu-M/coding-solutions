# Middle of Three

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given three distinct numbers a, b and c. Find the number with a value in the middle (Try to do it with minimum comparisons).

 **Examples :** 

```
Input: a = 978, b = 518, c = 300
Output: 518
Explanation: Since 518>300 and 518<978, so 518 is the middle element.
```

```
Input: a = 162, b = 934, c = 200
Output: 200
Exaplanation: Since 200>162 && 200<934, So, 200 is the middle element.

```

```
Input: a = 246, b = 214, c = 450
Output: 246
```

 **Constraints:** 
1<=a, b, c<=109
a, b, c are distinct.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T16:37:55.144Z  

```py
class Solution:
    def middle(self, a, b, c):
        #code here
        l = [a,b,c]
        l.sort()
        return l[1]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/middle-of-three2926/1)