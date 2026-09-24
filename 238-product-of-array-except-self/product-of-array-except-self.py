class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        answer = [1]*len(nums)

        left_product = 1
        right_product = 1

        for i in range(len(nums)):
            # Add current product to answer
            answer[i] = left_product
            # prep for the next iteration
            left_product *= nums[i] 

        for i in range(len(nums)-1, -1, -1):

            answer[i] *= right_product
            right_product *= nums[i] 

        return answer