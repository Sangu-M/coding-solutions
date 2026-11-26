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


        