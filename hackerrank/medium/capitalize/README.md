# Capitalize!

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, `alison heck` should be capitalised correctly as `Alison Heck`. 

$\color{red}\texttt{a}\color{black}\texttt{lison}\ \color{red}\texttt{h}\color{black}\texttt{eck}\ \color{black} \Rightarrow \color{black}\texttt{Alison}\ \color{black}\texttt{Heck}$

Given a full name, your task is to _capitalize_ the name appropriately.

**Input Format**

A single line of input containing the full name, $S$.

**Constraints**

+ $0 < len(S) < 1000$  
+ The string consists of alphanumeric characters and spaces.  

**Note:** in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc. 

**Output Format**

Print the capitalized string, $S$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T07:13:50.836Z  

```py


# Complete the solve function below.
def solve(s):
    return s.title()



```

---

[View on HackerRank](https://www.hackerrank.com/challenges/capitalize/problem)