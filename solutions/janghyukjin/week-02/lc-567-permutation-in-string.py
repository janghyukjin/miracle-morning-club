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
