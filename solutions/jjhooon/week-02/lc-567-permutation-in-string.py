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