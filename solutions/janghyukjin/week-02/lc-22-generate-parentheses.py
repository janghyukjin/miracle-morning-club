from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        res = []

        def make(arr, left_cnt, right_cnt):
            if left_cnt == right_cnt == n:
                res.append("".join(arr))
                return
            if left_cnt < n:
                arr.append("(")
                make(arr, left_cnt + 1, right_cnt)
                arr.pop()
            if left_cnt > right_cnt:
                arr.append(")")
                make(arr, left_cnt, right_cnt + 1)
                arr.pop()

        make(arr, 0, 0)
        return res
