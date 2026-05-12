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