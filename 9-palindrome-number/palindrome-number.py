class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)

        if len(x)%2 == 0:
            n = len(x)/2
        else:
            n = (len(x)+1)/2

        for i in range(int(n)):
            if x[i] != x[-(i+1)]:
                return False

        return True