class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        

        dpString ="#" + "#".join(s) + "#"

        dp = [0] * len(dpString)
        n = len(dpString)

        maxLength = 0
        maxString = s[0]
        center = 0
        right = 0

        for i in range(len(dpString)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(dpString) and dpString[i-dp[i]-1] == dpString[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > maxLength:
                maxLength = dp[i]
                maxString = dpString[i-dp[i]:i+dp[i]+1].replace('#','')
                
        return maxString
     
        