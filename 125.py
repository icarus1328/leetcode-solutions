class Solution:
    def isPalindrome(self, s: str) -> bool:
        out = ""
        i = 0
        while i < len(s):
            if s[i].isalnum():
                out += s[i].lower()
            i += 1
        return out[::-1] == out