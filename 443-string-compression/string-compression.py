class Solution:
    def compress(self, chars: list[str]) -> int:
        read = 0
        write = 0
        n = len(chars)
        chars.append("[")

        for i in range(n):
            if chars[i] != chars[i + 1]:
                group_length = i - read + 1
                read = i + 1

                chars[write] = chars[i]
                write += 1

                if group_length > 1:
                    for digit in str(group_length):
                        chars[write] = digit
                        write += 1

        return write