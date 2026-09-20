class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0)+1
        
        for c in t:
            counter[c] = counter.get(c, 0) -1
        
        for v in counter.values():
            if v != 0:
                return False
        return True