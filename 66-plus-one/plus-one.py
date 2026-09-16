class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        digits[-1] += 1
        # print(len(digits))

        for i in range(len(digits)-1, -1, -1):
            # print(i)
            if digits[i] > 9:
                digits[i] = digits[i] - 10
                if i != 0:
                    digits[i-1] = digits[i-1] + 1 
                else:
                    # print(digits)
                    digits[i] = 0
                    # print(digits)
                    digits.insert(0,1)
                    # print(digits)

        return digits
                