from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        answer = 0
        n = len(nums)
        nos_dict = defaultdict(int)
        
        for i in range(n):
            if nos_dict[k-nums[i]] and nos_dict[k-nums[i]] > 0:
                nos_dict[k-nums[i]] -= 1
                answer += 1
            else:
                nos_dict[nums[i]] = nos_dict.get(nums[i], 0) + 1

        return answer