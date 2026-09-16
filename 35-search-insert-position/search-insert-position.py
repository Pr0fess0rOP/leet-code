class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        if len(nums) < 2:
            if target <= nums[0]:
                return 0
            else:
                return 1
        
        if target <= nums[0]:
                return 0

        for i in range(len(nums)-1):
            if nums[i] == target:
                return i
            if target > nums[i] and target <= nums[i+1]:
                return i+1

        return len(nums)
            