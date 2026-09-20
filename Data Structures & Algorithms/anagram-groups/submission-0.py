class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams= {}
        res = []
        for string in strs:
            if tuple(sorted(string)) in anagrams:
                anagrams[tuple(sorted(string))].append(string)
            else:
                anagrams[tuple(sorted(string))] = [string]
        for an in anagrams:
            res.append(anagrams[an])
        return res