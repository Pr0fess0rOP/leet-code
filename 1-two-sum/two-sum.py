class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx1, num in enumerate(nums):
            
            if target-num in nums[idx1+1:]: # Find for idx 2 in rest of list
                
                # find the second index using index()
                idx2 = nums[idx1+1:].index(target-num) + idx1 + 1

                return [idx1, idx2]

        
        