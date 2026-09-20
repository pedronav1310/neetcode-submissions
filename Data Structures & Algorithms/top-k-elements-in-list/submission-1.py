class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        bucket=[[]for i in range(len(nums)+1)]
        for i in nums:
            freq[i] = freq.get(i, 0) +1

        for n, f in freq.items():
            bucket[f].append(n)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
        