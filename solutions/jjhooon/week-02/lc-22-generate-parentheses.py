class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(left, right, p):
            if len(p) == 2*n:
                answer.append(p)
                return

            if right > left:
                return

            if left < n:
                dfs(left + 1, right, p + "(")
            if right < n:
                dfs(left, right + 1, p + ")")

        dfs(0, 0, "")                
        return answer