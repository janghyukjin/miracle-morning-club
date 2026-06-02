class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        for i in s1:
            dic[i] = dic.get(i, 0) + 1
        i, j = 0, 0
        tmp = {}
        while j < len(s2):
            if s2[j] not in dic:
                tmp = {}
                j += 1
                i = j
                continue
            else:
                tmp[s2[j]] = tmp.get(s2[j], 0) + 1
                while tmp[s2[j]] > dic[s2[j]]:
                    tmp[s2[i]] -= 1
                    if tmp[s2[i]] == 0:
                        del tmp[s2[i]]
                    i += 1
            if tmp == dic:
                return True
            j += 1
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
