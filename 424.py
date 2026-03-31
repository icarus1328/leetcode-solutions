class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        max_freq = 0
        max_len = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in char_freq:
                char_freq[s[right ]] = 1
            else:
                char_freq[s[right]] += 1
            
            max_freq = max(max_freq, char_freq[s[right]])

            while right - left + 1 - max_freq > k:
                char_freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len