from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = Counter(t)
        size = len(count_t)
        check = 0
        left = 0

        # Window
        window = dict()
        window_size = float('inf')
        
        answer = ""

        for i in range(len(s)):
            char = s[i]
            window[char] = window.get(char, 0) + 1
            
            if char in count_t and window[char] == count_t[char]:
                check += 1

            while check == size:
                substring_size = i - left + 1

                if substring_size < window_size:
                    window_size = min(window_size, substring_size)
                    answer = s[left:i+1]
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in count_t and window[left_char] < count_t[left_char]:
                    check -= 1

                left += 1
        
        return answer


# ===== Interview Notes =====
# [Minimum Window Substring] Hard · Sliding Window + Frequency Match
#
# [접근법]
#   1. Variable sliding window — O(n) / O(Σ)
#      확장 → 매치되면 축소
#
# [Follow-up 질문 (면접 단골)]
#   - 중복 문자 t = 'AABC'에서 같은 A 두 개 필요한 경우?
#   - 여러 패턴 중 어느 하나라도 포함?
#   - 결과 substring 인덱스도 반환하면?
#
# [Pitfalls / 흔한 실수]
#   - have == need가 아니라 매칭된 문자 수로 비교
#   - window 시작/끝 인덱스 저장 (substring 반환용)
#
# [최적해 (참고)]
#   from collections import Counter
#   need = Counter(t)
#   have, required = {}, len(need)
#   l = matched = 0
#   best = (-1, -1, float('inf'))
#   for r, c in enumerate(s):
#       have[c] = have.get(c, 0) + 1
#       if c in need and have[c] == need[c]: matched += 1
#       while matched == required:
#           if r - l + 1 < best[2]: best = (l, r, r - l + 1)
#           have[s[l]] -= 1
#           if s[l] in need and have[s[l]] < need[s[l]]: matched -= 1
#           l += 1
#   return '' if best[2] == float('inf') else s[best[0]:best[1]+1]
# ===== End Interview Notes =====
