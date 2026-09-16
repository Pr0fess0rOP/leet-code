class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        substring = needle
        string = haystack

        if len(string) == len(substring):
            if string == substring:
                return 0
            else:
                return -1

        for i in range(len(string) - len(substring) + 1):
            
            if string[i] == substring[0]:
                print("First letter of substring matched!")
                print("Currently at i=", i)
                for j in range(len(substring)):
                    print("Currently at j=", j)
                    print("Currently at i+j=", i+j)
                    if substring[j] != string[i+j]:
                        break
                    if j == len(substring)-1:
                        return i
        
        return -1
            
                