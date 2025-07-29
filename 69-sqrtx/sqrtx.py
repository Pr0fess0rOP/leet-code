class Solution:
    def mySqrt(self, x: int) -> int:
        # Corner Case
        if x == 0:
            return 0
        
        left = 1
        right = x
        ans = 0
        while left <= right:
            
            mid = left + (right-left)//2
            square = mid*mid

            if square < x:
                ans = mid
                left = mid + 1

            elif square == x:
                return mid

            elif square > x:
                right = mid - 1

        return ans