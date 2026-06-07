# 풀이 실패

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slist = []

        for i in range(len(s)):
            substring = s[i]

            for j in range(i + 1, len(s)):
                if s[j] not in substring:
                    substring += s[j]
                else:
                    break

            slist.append(substring)

        if not slist:
            return 0

        slist = sorted(slist, key=lambda x: -len(x))
        return len(slist[0])


# ===== Interview Notes =====
# [Longest Substring Without Repeating Characters] Medium · Sliding Window + Set/Map
#
# [접근법]
#   1. Set sliding window — O(n) / O(min(n,Σ))
#      중복 발견 시 left 한 칸씩 이동
#   2. Map with last index (최적) — O(n) / O(min(n,Σ))
#      중복 시 left를 lastIdx+1로 점프
#
# [Follow-up 질문 (면접 단골)]
#   - k개까지 중복 허용?
#   - Unicode 처리?
#   - ASCII만이면 더 빠른 자료구조?
#
# [Pitfalls / 흔한 실수]
#   - left를 lastIdx+1로 할 때 max 처리 (뒤로 가지 않게)
#   - 빈 문자열 / 단일 문자
#
# [최적해 (참고)]
#   idx = {}
#   l = best = 0
#   for r, c in enumerate(s):
#       if c in idx and idx[c] >= l:
#           l = idx[c] + 1
#       idx[c] = r
#       best = max(best, r - l + 1)
#   return best
# ===== End Interview Notes =====
