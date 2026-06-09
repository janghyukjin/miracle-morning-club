from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(generated: str, remainingOpen: int, remainingClose: int):
            if remainingOpen == 0 and remainingClose == 0:
                result.append(generated)
            
            if remainingOpen > 0:
                dfs(generated+"(", remainingOpen -1, remainingClose+1)
            if remainingClose > 0:
                dfs(generated+")", remainingOpen, remainingClose-1)
            
        dfs("",n,0)
        return result


# ===== Interview Notes =====
# [Generate Parentheses] Medium · Backtracking
# URL: https://leetcode.com/problems/generate-parentheses/
#
# [힌트]
#   - 문자열을 왼쪽부터 만들어간다.
#   - open count는 n보다 작을 때만 추가 가능.
#   - close count는 open count보다 작을 때만 추가 가능.
#
# [체크]
#   - 종료 조건: 길이가 2*n일 때 결과에 추가.
#   - invalid 상태를 만들지 않으면 별도 validation이 필요 없다.
#   - 시간복잡도는 Catalan number 계열이라 단순 O(2^n)보다 더 정확히 설명 가능.
# ===== End Interview Notes =====
