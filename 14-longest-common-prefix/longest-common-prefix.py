class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = strs[0]

        for word in strs[1:]:

            for i in range( min( len(prefix), len(word) ) ):

                if word[i] != prefix[i]:
                    prefix = prefix[0:i]
                    break
                    
            if len(word) < len(prefix):
                prefix = prefix[0: len(word)]

        return prefix