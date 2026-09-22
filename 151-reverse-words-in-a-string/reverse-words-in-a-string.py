class Solution:
    def reverseWords(self, s: str) -> str:
        solution = s.strip().split()
        solution.reverse()
        print(solution)
        return " ".join(solution)