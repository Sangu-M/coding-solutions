# Greatest of Three Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given three numbers a, b and c. Find the greatest number among them.

 **Examples:** 

```
Input: a = 10, b = 3, c = 2
Output: 10
Explanation: 10 is greatest among the three 
```

```
Input: a = -4, b = -3, c = -2
Output: -2
Explanation: -2 is greatest among the three
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-20T15:50:53.092Z  

```py
a = int(input())
b = int(input())
c = int(input())

# code here
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/greatest-of-three-numbers2520/1)