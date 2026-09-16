class Solution:
    def mySqrt(self, x: int) -> int:

        # #Brute
        # if x == 1:
        #     return 1
        
        # i = 0
        # for i in range(x//2 + 1):
        #     if i*i == x:
        #         return i
        #     if i*i < x and (i+1)*(i+1) > x:
        #         return i
        #     i = i +1

        # Binary Search
        left = 0
        right = x
        answer = 0

        while left <= right:
            mid = (left + right)//2
        
            if mid*mid == x:
                return mid
            
            elif mid*mid > x:
                right = mid -1 
            
            elif mid*mid < x:
                answer = mid
                left = mid + 1

        return answer

        
                