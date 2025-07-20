class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest_word = min(strs, key=len)

        for i, char in enumerate(shortest_word):
            for word in strs:
                if word[i] != char:
                    return shortest_word[:i]
        
        return shortest_word
