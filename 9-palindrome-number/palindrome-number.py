class Solution(object):
    def isPalindrome(self, x):
        x_char = list(str(x))
        for i in range(len(x_char)//2):
            if x_char[i] != x_char[-(i+1)]:
                return False
        return True