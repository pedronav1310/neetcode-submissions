class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        l, r = 0, 0
        length=0
        while r < len(s):
            if s[r] in char:
                char.remove(s[l])
                l+=1
                
            else:
                char.add(s[r])
                r+=1
            length = max(length, r-l)

        return length