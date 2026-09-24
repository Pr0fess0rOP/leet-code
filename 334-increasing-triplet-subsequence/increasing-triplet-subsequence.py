class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        n = len(nums)

        if n < 3:
            return False


        curr = float('inf')
        maxx = float('-inf')
        minn = float('inf')
        

        for k in range(0, n, 1):

            if curr < nums[k]:
                return True
             
            if minn < nums[k]:
                curr = min(curr, nums[k])
            
            
            minn = min(nums[k], minn)

        return False
            

            