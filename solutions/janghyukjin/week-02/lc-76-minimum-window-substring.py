from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        cnt = Counter(t)
        dic = Counter()
        l = 0
        r = 0
        res = ""
        minimum = 10**5
        need = len(cnt)
        tmp = 0
        while r < len(s):
            if s[r] in cnt:
                dic[s[r]] = dic.get(s[r], 0) + 1
                if dic[s[r]] == cnt[s[r]]:
                    tmp += 1
            while tmp == need:
                if minimum > r - l + 1:
                    minimum = r - l + 1
                    res = s[l:r + 1]
                if s[l] in cnt:
                    dic[s[l]] -= 1
                    if dic[s[l]] < cnt[s[l]]:
                        tmp -= 1
                l += 1
            r += 1
        return res


# ===== Interview Notes =====
# [Minimum Window Substring] Hard · Sliding Window + Hash Map
#
# [접근법]
#   1. Sliding Window (have/need 카운터) — O(|s| + |t|) / O(|s| + |t|)
#      본인 풀이: cnt(t의 요구치) + dic(현재 윈도우 카운트),
#      need = 충족해야 할 unique char 수, tmp = 현재 충족된 char 수.
#      tmp == need 일 때만 l을 줄이며 최소 윈도우 갱신.
#
# [핵심 아이디어]
#   - r을 늘려 "충족"시키고, 충족된 동안 l을 줄여 "수축"한다.
#   - dic[c] == cnt[c] 가 되는 "정확히 맞는 순간"에만 tmp++ → 중복 카운트 방지.
#   - 수축할 때 dic[c] < cnt[c] 가 되는 순간에만 tmp-- → 대칭.
#
# [Follow-up 질문 (면접 단골)]
#   - t에 중복 문자가 있으면? (예: t="AABC") → Counter로 빈도까지 매칭해야 함.
#   - Unicode/ASCII 외 문자도 들어오면? → dict 기반이라 OK, 배열 기반이면 깨짐.
#   - 스트리밍으로 s가 들어온다면? → r 포인터만 전진, 동일 로직 유지.
#   - 모든 valid window를 반환하라면? → tmp == need 진입할 때마다 결과 누적.
#
# [Pitfalls / 흔한 실수]
#   - tmp 증감 조건을 `>=`로 쓰면 같은 문자 들어올 때마다 tmp가 늘어 망함. `==`가 맞음.
#   - len(s) < len(t) early return 빠뜨리기.
#   - minimum 초기값을 너무 작게 잡기 (10**5는 제약상 안전, float('inf')가 더 견고).
#   - res = s[l:r+1] 의 r+1 (inclusive 처리).
#
# [복잡도]
#   - Time: O(|s| + |t|)  (l, r 각자 한 번씩만 이동)
#   - Space: O(|s| + |t|) (Counter 두 개)
#
# [최적해 (참고) — 배열 기반 미세 최적화]
#   from collections import Counter
#   def minWindow(s, t):
#       if not t or not s: return ""
#       need, missing = Counter(t), len(t)
#       l = start = end = 0
#       for r, c in enumerate(s, 1):
#           missing -= need[c] > 0
#           need[c] -= 1
#           if not missing:
#               while l < r and need[s[l]] < 0:
#                   need[s[l]] += 1; l += 1
#               if not end or r - l < end - start:
#                   start, end = l, r
#               need[s[l]] += 1; missing += 1; l += 1
#       return s[start:end]
# ===== End Interview Notes =====
