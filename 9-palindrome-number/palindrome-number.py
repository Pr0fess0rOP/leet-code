class Solution(object):
    def isPalindrome(self, x):
        x_char = list(str(x))
        for i in range(len(x_char)//2):
            print("inside For")
            if x_char[i] != x_char[-(i+1)]:
                print("inside if")
                return False
        return True