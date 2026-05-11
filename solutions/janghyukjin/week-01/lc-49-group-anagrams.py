from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            arr[key].append(s)
        return list(arr.values())
