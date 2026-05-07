# 📚 풀이 공유 폴더

매일 푼 LeetCode 문제 풀이를 여기에 push하면 자동으로 출석 + 잔디 인증.

## 📂 폴더 규칙

```
solutions/
├── [본인-username]/
│   ├── week-01/
│   │   ├── lc-49-group-anagrams.md
│   │   ├── lc-49-group-anagrams.py        (또는 .go .java .ts 등)
│   │   ├── lc-347-top-k-frequent.md
│   │   └── lc-347-top-k-frequent.py
│   ├── week-02/
│   │   └── ...
│   └── notes/                              (자유 메모, 영어 STAR 등)
└── ...
```

## ✍️ 파일 명명 규칙

```
lc-{문제번호}-{문제제목 kebab-case}.{확장자}
```

예시:
- `lc-49-group-anagrams.md`
- `lc-347-top-k-frequent-elements.py`
- `lc-4-median-of-two-sorted-arrays.go`

## 📝 풀이 노트 템플릿 (.md)

```markdown
# LC 49 — Group Anagrams

- **난이도**: Medium
- **카테고리**: Arrays & Hashing
- **풀이 시간**: 25분
- **첫 시도 결과**: AC / WA / TLE

## 접근
[본인이 어떻게 생각했는지]

## 풀이
1. 각 string을 sorted(string)으로 키화
2. Map[string][]string 으로 group

## 시간 복잡도
- Time: O(n × k log k)
- Space: O(n × k)

## 배운 점 / 실수
- ...

## 다른 풀이 (있다면)
- 카운트 키 사용 시 O(n × k) 가능
```

## 🚀 시작 가이드

### 1. Repo 권한 받기 (관리자에게 요청)
관리자가 collaborator로 초대 → 본인 GitHub 계정에서 수락

### 2. Clone
```bash
git clone https://github.com/janghyukjin/miracle-morning-club.git
cd miracle-morning-club
```

### 3. 본인 폴더 만들기
```bash
mkdir -p solutions/[본인-github-username]/week-01
```

### 4. 풀이 push
```bash
# 풀이 작성 후
git add solutions/[본인-username]/
git commit -m "Week 1 - LC 49 Group Anagrams"
git push origin main
```

### 5. 자동 출석 확인
메인 페이지 "함께하기" 섹션에 본인 commit이 표시됨 (지난 30일).

## 🔥 잔디 만드는 팁

- 매일 1 commit 이상 → 매일 잔디 칠해짐
- commit message는 의미 있게 (e.g., "Week 1 Day 1 - LC 49 + 347")
- 풀이 + 노트 함께 push → 한번에 풍부하게

## ❓ FAQ

**Q: 풀이가 부끄러워서 망설여져요**
A: 모두 처음 풀어보는 거예요. 틀려도 OK, 푸는 시도가 중요. 다른 사람 풀이 보면서 배우는 게 핵심.

**Q: Premium 문제(LC 271 등)는?**
A: 문제 설명을 README에 적고 풀이만 push해도 OK.

**Q: 같은 문제 여러 풀이?**
A: 환영. `lc-49-group-anagrams-v2.py` 또는 한 파일에 여러 풀이 작성.
