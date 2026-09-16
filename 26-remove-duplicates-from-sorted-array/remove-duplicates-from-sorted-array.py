class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        pop_list = []

        for i in range(n-1, 0, -1):

            if nums[i] == nums[i-1]:
                pop_list.append(i)
        
        for idx in pop_list:
            nums.pop(idx)

        return len(nums)