from typing import List
import math


class Solution:
    def compress(self, chars: List[str]) -> int:
        char_counter = 1
        write_index = 0

        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i-1]:
                char_counter += 1
            else:
                chars[write_index] = chars[i-1]
                write_index += 1
                if char_counter > 1:
                    for digit in str(char_counter):
                        chars[write_index] = digit
                        write_index += 1
                char_counter = 1  # since we don't count very head of repeating char

        return write_index
