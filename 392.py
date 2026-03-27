class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        right = 0
        n = len(t)
        count = 0
        i = 0

        while i < len(s) and right < len(t):
            if s[i] == t[right]:
                count += 1
                right += 1
                i += 1
            else:
                right += 1
        return count == len(s)

        
        