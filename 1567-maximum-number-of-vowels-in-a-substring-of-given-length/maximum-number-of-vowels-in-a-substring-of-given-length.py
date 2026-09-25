class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vovel_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0,  'u': 0}
        count = 0
        answer = 0
        for i in range(k):
            if s[i] in vovel_dict:
                count += 1
        answer = count
        for i in range(k, len(s)):
            if s[i] in vovel_dict:
                count += 1
            
            if s[i-k] in vovel_dict:
                count -= 1
            answer = max(answer, count)
        return answer
