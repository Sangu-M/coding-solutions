# sWAP cASE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

__[str.isalnum()](https://docs.python.org/2/library/stdtypes.html#str.isalnum)__  
This method checks if all the characters of a string are alphanumeric *(a-z, A-Z and 0-9)*.
	
    >>> print 'ab123'.isalnum()
    True
    >>> print 'ab123#'.isalnum()
    False

---
__[str.isalpha()](https://docs.python.org/2/library/stdtypes.html#str.isalpha)__  
This method checks if all the characters of a string are alphabetical *(a-z and A-Z)*.

    >>> print 'abcD'.isalpha()
    True
    >>> print 'abcd1'.isalpha()
    False

---
__[str.isdigit()](https://docs.python.org/2/library/stdtypes.html#str.isdigit)__  
This method checks if all the characters of a string are digits *(0-9)*.

    >>> print '1234'.isdigit()
    True
    >>> print '123edsd'.isdigit()
    False

---
__[str.islower()](https://docs.python.org/2/library/stdtypes.html#str.islower)__  
This method checks if all the characters of a string are lowercase characters *(a-z)*.

    >>> print 'abcd123#'.islower()
    True
    >>> print 'Abcd123#'.islower()
    False
   
---
__[str.isupper()](https://docs.python.org/2/library/stdtypes.html#str.isupper)__  
This method checks if all the characters of a string are uppercase characters *(A-Z)*.

    >>> print 'ABCD123#'.isupper()
    True
    >>> print 'Abcd123#'.isupper()
    False

---
__Task__

You are given a string $S$.  
Your task is to find out if the string $S$ contains: *alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters*. 

**Input Format**

A single line containing a string $S$.

__Constraints__

$ 0 < len(S) < 1000 $


**Output Format**

In the first line, print `True` if $S$ has any *alphanumeric characters*. Otherwise, print `False`.  
In the second line, print `True` if $S$ has any *alphabetical characters*. Otherwise, print `False`.  
In the third line, print `True` if $S$ has any *digits*. Otherwise, print `False`.  
In the fourth line, print `True` if $S$ has any *lowercase characters*. Otherwise, print `False`.  
In the fifth line, print `True` if $S$ has any *uppercase characters*. Otherwise, print `False`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T17:22:56.847Z  

```py
def swap_case(s):
    s1 = s.swapcase()
    return s1


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/string-validators/problem)