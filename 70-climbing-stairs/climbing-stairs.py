class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # initial Values for step 3
        step_back_1_ways = 2 # Ways(2) for step 3
        step_back_2_ways = 1 # Ways(1) for step 3

        for i in range(3, n+1):
            #to reach step n, u need to know step n-1 and step n-2
            current_ways = step_back_1_ways + step_back_2_ways

            # move to next step
            step_back_2_ways = step_back_1_ways
            step_back_1_ways = current_ways
        
        return current_ways

