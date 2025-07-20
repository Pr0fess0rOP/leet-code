class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 == 1:
            return False

        bracket_dict = {')':'(', '}':'{', ']':'['}
        stack = []

        for bracket in s:
            # opening bracket append to stack
            if bracket in bracket_dict.values():
                stack.append(bracket)
                # print('closing', bracket)
            
            # closing bracket check for its latest openers
            elif bracket in bracket_dict.keys():
                # print('opening', bracket)
                if not stack or stack[-1] != bracket_dict[bracket]:
                    return False
                stack.pop()

        return not stack