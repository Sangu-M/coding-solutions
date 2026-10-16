# sWAP cASE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string and your task is to *swap cases*. In other words, convert all lowercase letters to uppercase letters and vice versa.

**For Example:**

    Www.HackerRank.com → wWW.hACKERrANK.COM
    Pythonist 2 → pYTHONIST 2  
    
    
**Function Description**   

Complete the *swap_case* function in the editor below.   

*swap_case* has the following parameters:   

- *string s:* the string to modify   

**Returns**   

- *string:* the modified string   

**Input Format**

A single line containing a string $s$.





**Constraints**

$0 \lt len(s) \le 1000$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T17:22:17.572Z  

```py
def swap_case(s):
    s1 = s.swapcase()
    return s1


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/swap-case/problem)