class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        left = 0
        right = 0
        while left<len(word1) or right<len(word2):
            if right==len(word2) or left>right:
                out += word1[left]
                left += 1 
            elif right>left or left==len(word1):
                out += word2[right]
                right += 1
            else:
                out += word1[left]
                out += word2[right]
                right += 1
                left += 1
            
        return out
