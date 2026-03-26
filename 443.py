class Solution:
    def compress(self, chars: List[str]) -> int:
        replace = 0
        i = 0

        while i < len(chars):
            curr = chars[i]
            count = 0
            while i < len(chars) and chars[i] == curr:
                count += 1
                i += 1
            
            chars[replace] = curr
            replace += 1

            if count > 1:
                for digit in str(count):
                    chars[replace] = digit
                    replace += 1
            
        return replace