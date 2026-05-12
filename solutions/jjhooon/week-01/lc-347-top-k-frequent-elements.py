from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) 
        count = sorted(count.items(), key=lambda x:-x[1])
        
        return [tmp[0] for i, tmp in enumerate(count) if i < k] 