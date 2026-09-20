class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams= {}
        res = []
        for string in strs:
            count = [0]*26
            for c in string:
                count[ord(c)-ord('a')]+=1

            key = tuple(count)
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
        return list(anagrams.values())