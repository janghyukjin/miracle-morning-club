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


# ===== Interview Notes =====
# [Longest Repeating Character Replacement] Medium · Sliding Window
#
# [접근법]
#   1. Sliding window + frequency — O(n) / O(Σ)
#      window size - maxCount <= k 조건 유지
#
# [Follow-up 질문 (면접 단골)]
#   - 최적 maxCount 갱신 시점은?
#   - k=0이면? (모든 문자 동일한 longest substring)
#   - 여러 종류 변경 허용하면?
#
# [Pitfalls / 흔한 실수]
#   - window 줄일 때 maxCount는 갱신 안 해도 OK (이미 그 길이 이상 보장)
#   - 26개 알파벳만이면 inner loop 무시 가능
#
# [최적해 (참고)]
#   cnt = {}
#   l = best = maxCnt = 0
#   for r, c in enumerate(s):
#       cnt[c] = cnt.get(c, 0) + 1
#       maxCnt = max(maxCnt, cnt[c])
#       if (r - l + 1) - maxCnt > k:
#           cnt[s[l]] -= 1
#           l += 1
#       best = max(best, r - l + 1)
#   return best
# ===== End Interview Notes =====
