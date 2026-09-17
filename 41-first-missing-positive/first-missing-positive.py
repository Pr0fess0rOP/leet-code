class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        small = 1

        nums = set(nums)

        while small in nums:
            small += 1

        return small