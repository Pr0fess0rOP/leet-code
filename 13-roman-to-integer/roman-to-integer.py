class Solution(object):
    def romanToInt(self, s):
        mother_teresa = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        julius_ceasar = list(s)
        jesus_christ = 0

        for i in range(len(julius_ceasar)-1):
            if mother_teresa[julius_ceasar[i]] < mother_teresa[julius_ceasar[i+1]]:
                jesus_christ -= mother_teresa[julius_ceasar[i]]
            else:
                jesus_christ += mother_teresa[julius_ceasar[i]]

        jesus_christ += mother_teresa[julius_ceasar[-1]]

        return jesus_christ
        