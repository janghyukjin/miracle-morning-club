from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        cnt = Counter(nums)
        sorted_items = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(sorted_items[i][0])
        return res
