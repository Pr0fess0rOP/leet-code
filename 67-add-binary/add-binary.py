class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        answer = []
        carry = 0

        for i in range(-1,-(min(len(a), len(b)) + 1), -1):

            addition = carry + int(a[i]) + int(b[i])

            if addition == 0:
                answer.insert(0, 0) 
                carry = 0
            if addition == 1:
                answer.insert(0, 1) 
                carry = 0
            if addition == 2:
                answer.insert(0, 0)
                carry = 1 
            if addition == 3:
                answer.insert(0, 1)
                carry = 1 

        for j in range(i- 1, -(max(len(a), len(b)) + 1), -1):
            if len(a) > len(b):
                addition = carry + int(a[j])
            else:
                addition = carry + int(b[j])

            if addition == 0:
                answer.insert(0, 0) 
                carry = 0
            if addition == 1:
                answer.insert(0, 1) 
                carry = 0
            if addition == 2:
                answer.insert(0, 0)
                carry = 1 
        
        if carry != 0:
            answer.insert(0,1)
            carry = 0

        return "".join(map(str, answer))
