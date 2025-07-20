class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_string = ''.join(map(str, digits))
        digits_number = int(digits_string) + 1
        new_string = str(digits_number)
        new_list = list(map(int, new_string))
        return new_list

