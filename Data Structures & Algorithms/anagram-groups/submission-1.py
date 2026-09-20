class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams= {}
        res = []
        for string in strs:
            key = "".join(sorted(string))
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
        for an in anagrams:
            res.append(anagrams[an])
        return res