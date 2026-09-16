class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        change_array = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                change_array.append(i)
                count += 1

        # print(change_array)
        for idx in reversed(change_array):
            nums.append(nums.pop(idx))

        # print(nums)
        return len(nums) - count