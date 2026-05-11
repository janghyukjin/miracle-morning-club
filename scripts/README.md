# 🤖 AI Interview Notes (Auto)

본인이 풀이 push하면 GitHub Action이 자동으로 Claude AI에게 분석 요청해서
파일 끝에 면접 노트를 주석으로 추가합니다.

## 작동 방식

```
[당신] git push solutions/janghyukjin/week-01/lc-49-group-anagrams.py
   ↓
[GitHub Action] 파일 감지 → Claude API 호출 → 분석 결과 받음
   ↓
[GitHub Action] 파일 끝에 주석으로 노트 append → 자동 commit + push
   ↓
[당신] git pull 하면 노트 추가된 파일 받음
```

## 노트 형식

각 풀이 파일 끝에 이런 식으로 붙음:

```python
class Solution:
    def groupAnagrams(self, strs):
        # ... 본인 풀이 ...

# ===== Interview Notes (AI-generated) =====
# [풀이 평가]
# 시간 O(n·k log k), 공간 O(n·k). sorted tuple key 방식은 가장 직관적이지만
# k가 클 때 sorted 비용이 큽니다.
#
# [최적해]
# Character count를 key로 쓰면 O(n·k)로 개선:
#     cnt = [0] * 26
#     for c in s: cnt[ord(c) - ord('a')] += 1
#     d[tuple(cnt)].append(s)
#
# [Follow-up 질문 3개]
# 1. sorting 없이 풀 수 있나요? → char count
# 2. k가 매우 크면? → count 방식이 더 유리
# 3. unicode 입력 처리? → dict 카운트
#
# [Pitfalls]
# - list는 hashable 아님 → tuple로 변환
# - 빈 문자열 edge case
# ===== End Interview Notes =====
```

## 셋업 (관리자만 1회)

1. Anthropic API key 발급: https://console.anthropic.com/settings/keys
2. Repo Settings → Secrets and variables → Actions → New secret
   - Name: `ANTHROPIC_API_KEY`
   - Value: `sk-ant-...` (발급받은 키)
3. 다음 push부터 자동 작동

## 비용

- Claude Sonnet 기준 풀이 1개당 약 $0.005 (7원)
- 한 달 평균 30 push 가정 시 약 1,000원
- API key 발급한 사람의 계정으로 청구됨

## 이미 push된 파일도 노트 받으려면

스크립트는 노트 마커가 없는 파일을 모두 처리하므로, 새 push 시
자동으로 백필됩니다. 또는 Actions 탭에서 "Run workflow" 수동 트리거 가능.

## 노트 다시 받기 (재분석)

파일에서 `===== Interview Notes` 부터 `===== End Interview Notes` 까지
지우고 push하면 새 분석을 받습니다.

## 무한 루프 방지

Action이 만든 commit은 `[skip notes]` 태그가 있어 자기 자신을 재트리거하지 않습니다.
