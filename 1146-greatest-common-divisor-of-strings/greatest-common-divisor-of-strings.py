class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        if n1 < n2:
            small = str1
            large = str2
        else:
            small = str2
            large = str1

        substring = ""

        for i in range(min(n1, n2), 0, -1):
            # print("i = ",i)
            # print(small[:i])
            if max(n1, n2) % i == 0:
                # print("% operator loop passed with value = ", small[:i]*int(max(n1, n2) / i))
                # print("large", large)
                if small[:i]*int(max(n1, n2) / i) == large and small[:i]*int(min(n1, n2) / i) == small:
                    substring = small[:i]
                    break

        return substring
                
                
