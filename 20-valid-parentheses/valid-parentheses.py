class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketMap = {"}": "{", ")": "(", "]": "["}

        bracket_queue = []

        for char in s:

            if char not in bracketMap:
                bracket_queue.append(char)

            if char in bracketMap:
                
                if len(bracket_queue) == 0:
                    return False
                else:
                    if bracket_queue[-1] != bracketMap[char]:
                        return False
                    else:
                        bracket_queue.pop()

        if len(bracket_queue) != 0:
            return False

        return True