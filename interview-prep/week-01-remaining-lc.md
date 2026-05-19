# Week 1 — 남은 2문제 풀이 가이드

본인이 직접 풀고 막힐 때 참고하는 가이드. **먼저 30분 혼자 풀기 → 막히면 힌트** 순서.

---

## 📝 LC 271 — Encode and Decode Strings (Medium)

### 문제 요약

문자열 리스트 → 하나의 문자열로 인코드 / 디코드 ↔ 원본 복원

```python
encode(["lint", "code", "love", "you"])  # → 어떤 문자열로 인코딩
decode(encoded_str)                       # → ["lint", "code", "love", "you"]
```

### 💡 힌트 (단계별 — 막혔을 때 한 줄씩)

<details>
<summary>힌트 1 — 단순 구분자 X</summary>

문자열 안에 어떤 문자라도 나올 수 있어서 `,` `;` `#` 같은 단순 구분자만 쓰면 ambiguous. 어떻게 구분?
</details>

<details>
<summary>힌트 2 — Length prefix</summary>

각 문자열 앞에 **길이 + 구분자**를 prefix로:
```
encode(["lint", "code"]) → "4#lint4#code"
```
디코드 시 `#` 찾고 → 길이 파싱 → 정확히 그만큼 잘라내기.
</details>

<details>
<summary>힌트 3 — Decode 알고리즘</summary>

포인터 `i = 0` 으로 시작:
1. `i`부터 `#` 찾기 → 길이 추출
2. `#` 다음부터 길이만큼 잘라서 result에 추가
3. `i` = `#` 다음 + 길이로 이동
4. 끝까지 반복
</details>

### ✅ 검증 케이스 (본인 풀이 테스트)

```python
# Case 1: 정상
assert decode(encode(["lint", "code", "love", "you"])) == ["lint", "code", "love", "you"]

# Case 2: 빈 리스트
assert decode(encode([])) == []

# Case 3: 빈 문자열 포함
assert decode(encode(["", "abc", ""])) == ["", "abc", ""]

# Case 4: 구분자 문자 포함
assert decode(encode(["a#b", "c#"])) == ["a#b", "c#"]

# Case 5: 매우 긴 문자열
long_s = "a" * 1000
assert decode(encode([long_s])) == [long_s]
```

### 🎤 면접 영어 설명 패턴

```
"My approach uses length-prefix encoding.

For each string, I prepend its length followed by a delimiter — I'll use '#'.
So ["lint", "code"] becomes "4#lint4#code".

This handles any character including the delimiter, because we always parse
the length first and read exactly that many characters.

Time complexity is O(n) for both encode and decode, where n is total characters.
Space is O(n) for the output.

An alternative would be a fixed-width length prefix or escaping, but
length-prefix is the cleanest."
```

### 🔗 본인 도메인 연결 (Follow-up 대비)

면접관: "이 패턴 실제로 어디서 봤어요?"
> "Yes, in Kubernetes CRD serialization — but in practice, we use Protobuf which uses length-prefix variable-length encoding for strings. The principle is the same."

---

## 📝 LC 128 — Longest Consecutive Sequence (Medium)

### 문제 요약

정렬 안 된 정수 배열에서 **가장 긴 연속 정수 수열** 길이. **O(n)** 필요.

```python
[100, 4, 200, 1, 3, 2]  # → 4 ([1,2,3,4])
```

### 💡 힌트 (단계별)

<details>
<summary>힌트 1 — Naive 접근 (먼저 떠올리되 X)</summary>

정렬 → O(n log n) → 옆 비교. 정답이지만 **문제가 O(n) 요구**.
</details>

<details>
<summary>힌트 2 — HashSet</summary>

모든 수를 HashSet에 → O(1) lookup. 어떻게 활용?
</details>

<details>
<summary>힌트 3 — 시작점만 처리</summary>

각 수 `x`에 대해 `x-1`이 set에 **없을 때만** 연속 수열 시작점.
시작점에서 `x, x+1, x+2, ...` 카운트.

이렇게 하면 각 수는 정확히 1번씩만 방문 = **O(n)**.
</details>

<details>
<summary>힌트 4 — 골격</summary>

```python
def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:  # 시작점만!
            current = n
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest
```
</details>

### ✅ 검증 케이스

```python
assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert longestConsecutive([]) == 0
assert longestConsecutive([0]) == 1
assert longestConsecutive([1, 2, 0, 1]) == 3  # 중복 처리
assert longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]) == 7  # [-1..5? 아니다, 3..9]
```

### 🎤 면접 영어 설명 패턴

```
"The naive approach would sort and scan — O(n log n). But the problem
specifies O(n), so we need a different approach.

My approach uses a HashSet for O(1) lookups.

The key insight: for each number, I only start counting if it's the start
of a sequence — meaning n-1 is NOT in the set. This way, each number is
visited at most twice — once when we check, once when we count forward.

Total time complexity is O(n), space is O(n) for the set.

If we don't do the 'start of sequence' check, the worst case becomes O(n²)
because we'd recount overlapping sequences."
```

### 🔗 본인 도메인 연결

면접관: "이게 실제로 어디 쓰여요?"
> "Range queries on sparse data. For example, in monitoring, detecting consecutive missing timestamps in a metric series. Or in resource allocation, finding the longest contiguous block of free IDs."

---

## 🎯 풀이 후 체크리스트

각 문제 풀고 나서:

```
□ 본인 풀이 시간 측정 (실제 인터뷰는 25-30분)
□ 검증 케이스 모두 통과
□ Time/Space complexity 명시
□ 영어로 5분 설명 녹음
□ Follow-up 질문 1개 추가 생각
□ solutions/janghyukjin/week-01/ 에 commit
```

---

## 📅 다음 단계

Week 1 완료 후:

| Week | 주제 | 추천 문제 |
|---|---|---|
| Week 2 | Two Pointers | LC 125, LC 167, LC 15, LC 11 |
| Week 3 | Sliding Window | LC 121, LC 3, LC 424, LC 76 |
| Week 4 | Stack | LC 20, LC 22, LC 150, LC 84 |
| Week 5 | Binary Search | LC 704, LC 33, LC 153, LC 4 |
| Week 6 | Linked List | LC 206, LC 21, LC 143, LC 23 |

각 주제별 4-5문제, 총 24-30문제 / 6주 = **하루 1문제 페이스**.
