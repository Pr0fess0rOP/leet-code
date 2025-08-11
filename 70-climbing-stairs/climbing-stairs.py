class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev = 1
        prev2 = 0

        for _ in range(1, n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr

        return prev