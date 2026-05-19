# 풀이 실패
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += (str(len(s)) + "=" + s)
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "=":
                j += 1
            
            tmp = int(s[i:j])
            i = j + 1
            j = i + tmp
            
            result.append(s[i:j])
            i = j

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
#   Q: 입력에 임의의 문자 포함되면?
#   A: Length-prefix 방식이면 OK. 길이를 먼저 읽고 그만큼 정확히 잘라내니 어떤 문자가 와도 안전. 단순 ',' 같은 delimiter만 쓰면 conflict 발생.
#
#   Q: 메모리 효율은? (큰 문자열)
#   A: encode는 list + join (O(n)). decode는 slicing 없이 포인터 i, j만 들고가서 in-place 파싱. 추가 메모리는 결과 배열만.
#
#   Q: 분산 환경에서 안전한 인코딩은?
#   A: Protocol Buffers나 MessagePack 같은 표준 binary serialization 권장. UTF-8 + length-prefix는 cross-language 안전. JSON은 escape 처리 비용.
#
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
