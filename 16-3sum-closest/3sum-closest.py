class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2] 
        
        # Brute Force
        # for i in range(n-2):  
        #     for j in range(i+1, n-1):  
        #         for k in range(j+1, n):
        #             current_sum = nums[i] + nums[j] + nums[k] 
        #             if abs(target - closest_sum) > abs(target - current_sum): 
        #                 closest_sum = current_sum 

        # 1 loop and 2 pointers
        nums.sort()
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right] 

                # If we got the exact match, return that
                if current_sum == target:
                    return target

                # if sum is not equal then check if the new sum is better than our best answer
                if abs(target - closest_sum) > abs(target - current_sum):
                    closest_sum = current_sum

                # Decide the movement of left and right inside the subarray
                
                # if true, means my num combo needs a smaller number
                # Since array is sorted, i can move "right" to a less index for a smaller number
                if current_sum > target: 
                    right -= 1
                # since we already check 
                # Since array is sorted, i can move "left" to a less index for a bigger number
                else:
                    left += 1

        return closest_sum