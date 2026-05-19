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


# ===== Interview Notes =====
# [Encode and Decode Strings] Medium · String Serialization
#
# [접근법]
#   1. Length-prefix (최적) — O(n)
#      '{len}#{string}' 포맷
#   2. Non-ASCII delimiter — O(n)
#      특수 문자 (chr(257) 등)로 join
#   3. Escape character — O(n)
#      구분자 충돌 시 escape, 복잡함
#
# [Follow-up 질문 (면접 단골)]
#   - 입력에 임의의 문자 포함되면?
#   - 메모리 효율은? (큰 문자열)
#   - 분산 환경에서 안전한 인코딩은?
#
# [Pitfalls / 흔한 실수]
#   - 빈 문자열 처리 ('0#')
#   - 단순 구분자는 conflict 위험
#   - decode 시 인덱스 관리 실수
#
# [최적해 (참고)]
#   # encode:
#   return ''.join(f'{len(s)}#{s}' for s in strs)
#   # decode:
#   res, i = [], 0
#   while i < len(s):
#       j = s.index('#', i)
#       n = int(s[i:j])
#       res.append(s[j+1:j+1+n])
#       i = j + 1 + n
#   return res
# ===== End Interview Notes =====
