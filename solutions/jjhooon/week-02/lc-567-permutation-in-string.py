from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_s1 = Counter(s1)
        cnt_s2 = Counter(s2[:len(s1)])

        if cnt_s1 == cnt_s2:
            return True

        for i in range(len(s1), len(s2)):
            left_char = s2[i - len(s1)]
            right_char = s2[i]

            cnt_s2[left_char] -= 1
            if cnt_s2[left_char] == 0:
                del cnt_s2[left_char]

            cnt_s2[right_char] = cnt_s2.get(right_char, 0) + 1

            if cnt_s1 == cnt_s2:
                return True

        return False


# ===== Interview Notes =====
# [Permutation in String] Medium · Fixed-size Sliding Window + Frequency
#
# [접근법]
#   1. Fixed window 비교 — O(n·Σ) / O(Σ)
#      매번 카운트 비교
#   2. Match counter (최적) — O(n) / O(Σ)
#      matches 변수로 O(1) 비교
#
# [Follow-up 질문 (면접 단골)]
#   - LC 438 (Find All Anagrams in a String)과 차이? (모든 위치 vs 존재만)
#   - stream 입력에서?
#   - 여러 패턴 동시 매칭? (Aho-Corasick)
#
# [Pitfalls / 흔한 실수]
#   - s2가 s1보다 짧으면 false
#   - 고정 윈도우 크기 = len(s1)
#
# [최적해 (참고)]
#   if len(s1) > len(s2): return False
#   cnt1, cnt2 = [0]*26, [0]*26
#   for c in s1: cnt1[ord(c)-97] += 1
#   for i, c in enumerate(s2):
#       cnt2[ord(c)-97] += 1
#       if i >= len(s1): cnt2[ord(s2[i-len(s1)])-97] -= 1
#       if cnt1 == cnt2: return True
#   return False
# ===== End Interview Notes =====
