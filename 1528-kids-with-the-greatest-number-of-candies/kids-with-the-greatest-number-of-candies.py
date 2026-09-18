class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n = len(candies)
        max_candies = max(candies)
        answer = []
        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer
                