class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        n = len(nums)

        if n < 3:
            return False

        max_array = [0]*n
        min_array = [0]*n

        maxx = float('-inf')
        minn = float('inf')
        
        for i in range(n):
            minn = min(nums[i], minn)
            min_array[i] = minn
        
        for j in range(n-1, -1, -1):
            maxx = max(nums[j], maxx)
            max_array[j] = maxx

        for k in range(1, n-1, 1):
            print(i)
            if  min_array[k-1] < nums[k] < max_array[k+1]:
                return True
            
        return False
            

            

            # for j in range(i+1, n-1):
            #     for k in range(j+1, n):
                    