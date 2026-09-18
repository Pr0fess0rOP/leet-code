class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Brute Force
        # solution = set()
        # n= len(nums)
        # for i in range(n-3):
        #     for j in range(i+1, n-2):
        #         for k in range(j+1, n-1):
        #             for l in range(k+1, n):
        #                 sums = nums[i] + nums[j] + nums[k] + nums[l]
        #                 if sums == target:
        #                     solution.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))

        # return list(solution)

        # 2 loop 2 pointer (3sum method)
        solution = set()
        n= len(nums)
        nums.sort()
        for i in range(n-3):
            for j in range(i+1, n-2):
                

                left = j+1
                right = n-1
                
                while left < right:
                    sums = nums[i] + nums[j] + nums[left] + nums[right]

                    if target == sums:
                        solution.add(
                            tuple(
                                sorted(
                                    [ 
                                        nums[i], nums[j], nums[left], nums[right] 
                                    ]
                                )
                            )
                        )
                        left += 1
                        right -= 1
                    
                    if sums > target:
                        right -= 1
                    if sums < target:
                        left += 1

                
        return list(solution)
