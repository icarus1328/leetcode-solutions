class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        index = []
        p_freq = {}
        s_freq = {}
        left = 0
        
        for i in range(len(p)):
            if p[i] not in p_freq:
                p_freq[p[i]] = 1
            else:
                p_freq[p[i]] += 1
        
        for right in range(len(s)):
            if s[right] not in s_freq:
                s_freq[s[right]] = 1
            else:
                s_freq[s[right]] += 1
            
            if right - left + 1 == len(p):
                if s_freq == p_freq:
                    index.append(s[left])
                s_freq[s[left]] -= 1
                if s_freq[s[left]] == 0:
                    del s_freq[s[left]]
                left += 1
        
        return index