# Maximum Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, find the subarray with the largest sum, and return  *its sum*.

 

Original
Python
 **Example 1:** 

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

```

 **Example 2:** 

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

```

 **Example 3:** 

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104

 

 **Follow up:**  If you have figured out the `O(n)` solution, try coding another solution using the  **divide and conquer**  approach, which is more subtle.

## Solution

**Language:** Python  
**Runtime:** 63 ms (beats 74.03%)  
**Memory:** 21 MB (beats 88.65%)  
**Submitted:** 2026-11-26T18:55:19.412Z  

```py
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum,currSum)
            if currSum < 0:
                currSum = 0
                continue
        return maxSum 


        
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-subarray/)