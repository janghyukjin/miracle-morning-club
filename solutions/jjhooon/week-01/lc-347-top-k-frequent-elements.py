from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) 
        count = sorted(count.items(), key=lambda x:-x[1])
        
        return [tmp[0] for i, tmp in enumerate(count) if i < k] 


# ===== Interview Notes =====
# [Top K Frequent Elements] Medium · Heap / Bucket Sort
#
# [접근법]
#   1. Sort — O(n log n) / O(n)
#      본인 풀이
#   2. Heap (안전판) — O(n log k) / O(n+k)
#      heapq.nlargest(k, cnt.keys(), key=cnt.get)
#   3. Bucket Sort (최적) — O(n) / O(n)
#      빈도를 인덱스로 하는 버킷 활용
#
# [Follow-up 질문 (면접 단골)]
#   - O(n log n)보다 빠르게? (→ heap 또는 bucket)
#   - k=1일 때 더 빠른 방법? (단순 max)
#   - 스트리밍 데이터에서?
#
# [Pitfalls / 흔한 실수]
#   - 동률 처리 (tied frequencies)
#   - k > unique 원소 수 edge case
#
# [최적해 (참고)]
#   from collections import Counter
#   cnt = Counter(nums)
#   buckets = [[] for _ in range(len(nums) + 1)]
#   for num, freq in cnt.items():
#       buckets[freq].append(num)
#   res = []
#   for i in range(len(buckets) - 1, 0, -1):
#       res.extend(buckets[i])
#       if len(res) >= k: return res[:k]
# ===== End Interview Notes =====
