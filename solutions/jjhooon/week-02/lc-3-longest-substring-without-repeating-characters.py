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