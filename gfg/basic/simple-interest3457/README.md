# Simple Interest

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given three integers  **p**,  **r** and  **t**, denoting Principal, Rate of Interest and Time period respectively. Calculate and print the Simple Interest.

 **Examples:** 

```
Input: p = 100, r = 20, t = 2
Output: 40.00
Explanation: The simple interest on 100 at a rate of 20% across 2 time periods is 40.
```

```
Input: p = 999, r = 9, t = 9
Output: 809.19
Explanation: The simple interest on 999 at a rate of 9% across 9 time periods is 809.19
```

 **Constraints:** 
1 ≤ p ≤ 105
1 ≤ r, t ≤ 100

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T16:23:31.504Z  

```py
p = int(input())
r = int(input())
t = int(input())

# code here
si = float()
si = (p*t*r)/100
print(f"{si:.2f}")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/simple-interest3457/1)