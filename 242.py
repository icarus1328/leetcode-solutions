class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] not in char_map:
                    char_map[s[i]] = 1
                else:
                    char_map[s[i]] += 1
            
            for j in range(len(t)):
                if t[j] not in char_map:
                    return False
                else:
                    char_map[t[j]] -= 1
                    if char_map[t[j]] == -1:
                        return False
        else:
            return False

        for chk in char_map.values():
            if chk != 0:
                return False
            return True