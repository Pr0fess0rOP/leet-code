class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        # Iterate the list
        for right in range(n):

            # if the charcter is not seen before...
            if s[right] not in charSet:
                # Add it to our collection
                charSet.add(s[right])
                currentLength = right - left + 1
                # Update max Length of substring
                maxLength = max(maxLength, currentLength) # plus one cause length starts at 1 not 0 
            # If the character is seen before...
            else:
                # check where the repetition starts
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left+=1
                charSet.add(s[right])
        return maxLength