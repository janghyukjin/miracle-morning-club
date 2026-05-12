from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = map(
            lambda x: x[0],
            sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        )

        return list(result)[:k]
