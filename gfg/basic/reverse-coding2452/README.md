# Sum of Natural Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an integer  **n**, compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.

 **Examples:** 

```
Input: n = 6
Output: 21
Explanation: The sum of natural numbers up to 6 is: 1 + 2 + 3 + 4 + 5 + 6 = 21.
```

```
Input: n = 4
Output: 10
Explanation: The sum of natural numbers up to 4 is: 1 + 2 + 3 + 4 = 10.
```

```
Input: n = 0
Output: 0
Explanation: Since n is 0, the sum is 0.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T17:38:20.499Z  

```py
n = int(input())
result = 0

# code here
for i in range(n+1):
    result += i
    
print(result)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/reverse-coding2452/1)