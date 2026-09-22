class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        reversing_letters = []
        reversing_index = []
        answer = ""
        vovel_dict = {'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}

        for idx, char in enumerate(s):

            if char in vovel_dict.keys() or char in vovel_dict.values():
                reversing_letters.append(char)
                reversing_index.append(idx)

        for i in range(len(reversing_index)):

            s[reversing_index[i]] = reversing_letters[len(reversing_index) - i - 1]
            
        return ''.join(s)

        # print(reversing_letters, reversing_index)
