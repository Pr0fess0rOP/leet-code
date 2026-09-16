class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        n1 = len(word1)
        n2 = len(word2)
        for i in range(min(n1, n2)):
            print(word1[i])
            print(word2[i])
            answer += word1[i]
            answer += word2[i]
    
        if n1 > n2:
            answer += word1[i+1:]
        else:
            answer += word2[i+1:]

        print(answer)
        return answer