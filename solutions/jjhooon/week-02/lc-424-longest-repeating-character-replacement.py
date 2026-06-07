# 풀이 실패

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        counter = {}
        start, end = 0, 0

        while end < len(s):
            counter[s[end]] = counter.get(s[end], 0) + 1

            while end - start + 1 - max(counter.values()) > k:
                counter[s[start]] -= 1
                start += 1

            max_len = max(end - start + 1, max_len)
            end += 1

        return max_len


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
