class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        dic = {}
        if length < 1:
            return length
        i = 0
        dic[s[i]] = 1
        res, cnt = 1, 1
        for j in range(1, length):
            res = max(res, cnt)
            dic[s[j]] = dic.get(s[j], 0) + 1
            if dic[s[j]] != 2:
                cnt += 1
                continue
            while dic[s[j]] == 2:
                if dic[s[i]] != dic[s[j]]:
                    cnt -= 1
                dic[s[i]] -= 1
                i += 1
        res = max(res, cnt)
        return res


# ===== Refined (리뷰 후 정리, 동일 알고리즘) =====
# 본인 풀이의 count-based sliding window 그대로 유지하고
# 보조변수(cnt, 초기화 분기, dual-branch) 만 제거.
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         dic = {}
#         left = res = 0
#         for right in range(len(s)):
#             dic[s[right]] = dic.get(s[right], 0) + 1
#             while dic[s[right]] > 1:
#                 dic[s[left]] -= 1
#                 left += 1
#             res = max(res, right - left + 1)
#         return res
#
# 변경점:
#   - cnt 삭제 → 윈도우 길이는 right - left + 1
#   - `if dic[s[i]] != dic[s[j]]: cnt -= 1` 의 비직관적 로직 사라짐
#   - length<1 early return 불필요 (range(0)이 빈 루프)
#   - dic[s[0]]=1 사전 초기화 불필요 (range(0,n) 부터 동일하게 처리)
#   - 두 분기(!=2, ==2) → while 하나로 통일


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
