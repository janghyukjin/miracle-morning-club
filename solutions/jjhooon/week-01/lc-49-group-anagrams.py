class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        dic = {}
        for s in strs:
            ss = sorted(s)
            ss = ''.join(ss)

            if ss not in dic:
                dic[ss] = [s]
            else:
                dic[ss].append(s)

        return [v for _, v in dic.items()]


# ===== Interview Notes =====
# [Group Anagrams] Medium · Hash Map + Sorting/Counting
#
# [접근법]
#   1. Sorted tuple key — O(n·k log k) / O(n·k)
#      tuple(sorted(s))를 dict key로
#   2. Character count key (optimal) — O(n·k) / O(n·k)
#      [0]*26 카운트 배열을 tuple로
#
# [Follow-up 질문 (면접 단골)]
#   - sort 없이 풀 수 있나? (→ char count)
#   - k(문자열 길이)가 매우 크면?
#   - Unicode/non-ASCII 처리는?
#
# [Pitfalls / 흔한 실수]
#   - list는 hashable 아님 → tuple로 변환
#   - 대소문자 구분 (Abc vs abc)
#
# [최적해 (참고)]
#   from collections import defaultdict
#   d = defaultdict(list)
#   for s in strs:
#       cnt = [0] * 26
#       for c in s: cnt[ord(c) - ord('a')] += 1
#       d[tuple(cnt)].append(s)
#   return list(d.values())
# ===== End Interview Notes =====
