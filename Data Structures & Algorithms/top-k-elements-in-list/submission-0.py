class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num]+=1
        
        a = sorted(freq, key=lambda num:freq[num], reverse=True)
        
        return a[:k]