# LC 49 — Group Anagrams

- **난이도**: Medium
- **카테고리**: Arrays & Hashing
- **링크**: https://leetcode.com/problems/group-anagrams/

## 접근
- Anagram끼리 같은 키를 갖도록 정렬해서 그루핑
- 또는 char count 26개 tuple을 키로 사용

## 풀이 방법 1: 정렬 키
```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```
- Time: O(n × k log k)
- Space: O(n × k)

## 풀이 방법 2: 카운트 키 (더 빠름)
```python
def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())
```
- Time: O(n × k)
- Space: O(n × k)

## 배운 점
- defaultdict로 group 만들 때 코드가 깔끔
- Python tuple은 dict 키로 hashable

## 영어 30초 설명
> "I used a hashmap where the key represents the sorted form of each string,
> so anagrams produce the same key. The values are lists of strings sharing
> that key. Time complexity is O(n times k log k) where n is the array length
> and k is the average string length."
