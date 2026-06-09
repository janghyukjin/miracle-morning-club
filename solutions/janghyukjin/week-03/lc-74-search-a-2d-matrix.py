from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                nums.append(matrix[i][j])
        right = len(nums) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


# ===== Interview Notes =====
# [Search a 2D Matrix] Medium · Binary Search (2D → 1D)
#
# [접근법]
#   1. Flatten + Binary Search — O(m*n) time / O(m*n) space  ← 본인 풀이
#      행렬을 1D 배열로 펼친 뒤 이분 탐색. 정답은 나오지만 **flatten 자체가 O(m*n)**
#      이라 이분 탐색의 의미가 사라짐. 면접에선 "왜 굳이 펼쳤어?" 질문 나옴.
#   2. 1D Index 매핑 (정석) — O(log(m*n)) / O(1)
#      행렬을 펼치지 않고 인덱스만 가상으로 매핑.
#      mid_val = matrix[mid // n][mid % n]
#   3. Two Binary Searches — O(log m + log n) / O(1)
#      먼저 "target이 속할 행"을 이분 탐색(각 행의 첫 원소 기준),
#      그 다음 해당 행 안에서 이분 탐색.
#   4. Staircase Search (LC 240 류) — O(m + n) / O(1)
#      우상단(또는 좌하단)에서 시작해 크면 왼쪽, 작으면 아래로.
#      LC 74의 "각 행 시작 > 이전 행 끝" 강한 정렬에선 1번보다 느리지만,
#      LC 240(약한 정렬)에선 이게 정석.
#
# [핵심 아이디어 — 인덱스 매핑 트릭]
#   - m행 n열 행렬에서 0 ≤ k < m*n 이라 할 때,
#     k번째 원소 = matrix[k // n][k % n]
#   - 이로써 "공간 추가 없이" 1D 이분 탐색을 그대로 적용 가능.
#
# [Follow-up 질문 (면접 단골)]
#   - flatten 안 하고 풀 수 있나? → 1D index 매핑 (필수 답변).
#   - 각 행의 첫 원소만 정렬되어 있고 행 간 강한 관계 없으면? → LC 240, staircase.
#   - 메모리 제약이 매우 빡세면? → O(1) 추가 공간만 쓰는 풀이 요구.
#   - target이 여러 개 있을 수 있다면? → lower_bound/upper_bound로 구간 반환.
#
# [Pitfalls / 흔한 실수]
#   - flatten으로 풀면 시간복잡도가 O(log) 가 아니라 O(m*n). "이분 탐색 문제"라는
#     문제 의도와 어긋남.
#   - 빈 행렬 / 빈 행 처리 (matrix == [] or matrix[0] == []).
#   - n = len(matrix[0]) 을 매번 계산하지 말고 상수로 잡기.
#
# [복잡도 비교]
#   - 본인 풀이:  Time O(m*n)         / Space O(m*n)
#   - 1D 매핑:    Time O(log(m*n))    / Space O(1)
#   - Two BS:     Time O(log m+log n) / Space O(1)   ※ 같은 O(log(m*n))
#
# [최적해 (참고) — 1D index 매핑]
#   def searchMatrix(matrix, target):
#       if not matrix or not matrix[0]: return False
#       m, n = len(matrix), len(matrix[0])
#       lo, hi = 0, m * n - 1
#       while lo <= hi:
#           mid = (lo + hi) // 2
#           val = matrix[mid // n][mid % n]
#           if val == target: return True
#           elif val < target: lo = mid + 1
#           else: hi = mid - 1
#       return False
# ===== End Interview Notes =====
