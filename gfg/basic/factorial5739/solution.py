class Solution:
    def factorial(self, n: int) -> int:
        # code here
        result = 1
        for i in range(n):
            result = result*(i+1)
        return result