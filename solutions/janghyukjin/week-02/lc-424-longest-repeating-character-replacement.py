class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        i = 0
        res, max_count = 0, 0
        for j in range(len(s)):
            dic[s[j]] = dic.get(s[j], 0) + 1
            max_count = max(max_count, dic[s[j]])
            while (j - i + 1) - max_count > k:
                dic[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
