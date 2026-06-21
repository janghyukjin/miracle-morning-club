


# ===== Interview Notes =====
# [Search a 2D Matrix] Medium · Binary Search (flattened)
#
# [접근법]
#   1. Row then column — O(log m + log n)
#      두 번 이진탐색
#   2. Single binary search (최적) — O(log(m·n))
#      1D 인덱스 → mid // cols, mid % cols
#
# [Follow-up 질문 (면접 단골)]
#   - LC 240 (각 행 정렬 + 각 열 정렬 but global X)와 차이?
#   - k번째 작은 원소는?
#   - 특정 범위 카운트는?
#
# [Pitfalls / 흔한 실수]
#   - row-major vs column-major 인덱싱
#   - 빈 행렬 edge case
#
# [최적해 (참고)]
#   rows, cols = len(matrix), len(matrix[0])
#   l, r = 0, rows * cols - 1
#   while l <= r:
#       mid = l + (r - l) // 2
#       val = matrix[mid // cols][mid % cols]
#       if val == target: return True
#       elif val < target: l = mid + 1
#       else: r = mid - 1
#   return False
# ===== End Interview Notes =====
