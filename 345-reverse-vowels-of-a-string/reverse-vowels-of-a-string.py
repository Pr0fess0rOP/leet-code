class Solution:
    def reverseVowels(self, s: str) -> str:

        # two-phase / auxiliary-array approach
        # O(n)
        # s = list(s)
        # reversing_letters = []
        # reversing_index = []
        # answer = ""
        # vovel_dict = {'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}

        # for idx, char in enumerate(s):

        #     if char in vovel_dict.keys() or char in vovel_dict.values():
        #         reversing_letters.append(char)
        #         reversing_index.append(idx)

        # for i in range(len(reversing_index)):

        #     s[reversing_index[i]] = reversing_letters[len(reversing_index) - i - 1]
            
        # return ''.join(s)


        # Two Pointer Approach
        s = list(s)
        vowels = "aeiouAEIOU"
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] in vowels:   
                if s[right] in vowels:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1  
            else:
                left += 1

        return ''.join(s)

            