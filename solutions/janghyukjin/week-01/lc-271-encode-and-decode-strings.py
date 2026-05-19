from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            length = len(strs[i])
            result += str(length) + "@" + strs[i]
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        while len(s) > 0:
            i = 0
            length = ""
            while s[i] != "@":
                length += s[i]
                i += 1
            result.append(s[i+1:i+int(length)+1])
            s = s[i+int(length)+1:]
        return result
