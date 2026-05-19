# Company Cheatsheet — Interview Process by Company

본인 타깃 회사별 라운드/문제 유형/팁 정리.

---

## 🥇 Step 3 — 메인 카드

### TikTok / ByteDance SG

| 항목 | 내용 |
|---|---|
| 라운드 수 | 4-6 |
| 일정 | 4-8주 |
| 코딩 난이도 | LC Medium-Hard 중심 (Top K, Heap, Graph, DP 자주) |
| 시스템 디자인 | 큰 비중 — 분산 시스템, 대규모 ML serving |
| Behavioral | "Five Whys" 깊이 파고드는 스타일 |
| 영어 환경 | 면접관 만다린/영어 혼재 가능 (영어 요청 가능) |
| 본인 어필 포인트 | LLMInferenceService 멀티노드 + mlx-operator |
| 보상 협상 | Levels.fyi 기반 leveling. 2-2 (시니어): SGD 200K, 3-1 (Staff): SGD 326K |

**자주 나오는 LC 패턴**:
- LRU Cache (Design)
- Word Search II (Trie)
- Top K Frequent Elements
- Course Schedule (Graph)
- Word Ladder II (BFS + 경로 복원)

**SD 자주 나오는 주제**:
- Design TikTok feed ranking system
- Design large-scale LLM inference platform
- Design global content moderation system

**팁**: "사장님 면접" (Hiring Manager Bar Raiser) 추가 가능. 본인이 자기 결정한 trade-off 깊이 변호할 수 있어야 함.

---

### Apple SG

| 항목 | 내용 |
|---|---|
| 라운드 수 | 4-5 |
| 코딩 난이도 | LC Medium 중심, behavioral 비중 ↑↑ |
| 시스템 디자인 | 1회, privacy/security 강조 |
| Behavioral | "Tell me about a time..." 매우 다양, deep dive |
| 영어 환경 | 100% 영어 |
| 본인 어필 | mlx-operator main + LINE DBaaS 대규모 (40K VM) |
| 컬쳐 | "Excellence at scale", attention to detail |

**팁**: Apple은 behavioral 한 라운드 통째로. STAR 답변 10개 완벽 외워야.

---

### Anthropic Tokyo

| 항목 | 내용 |
|---|---|
| 라운드 수 | 5-6 |
| 코딩 난이도 | LC Medium-Hard + take-home (2-4시간) |
| 시스템 디자인 | LLM serving / RL infra 도메인 깊음 |
| Behavioral | Mission-fit 매우 중요 (AI safety 진정성) |
| 본인 어필 | LLMInferenceService + HyperCLOVA X 기여 |
| 보상 | $300-500K (4.2-7억) ⭐ |

**팁**: 코딩 인터뷰가 production-grade. clean code + tests + edge case 모두 체크.

---

## 🥈 Step 2 — 실전 카드

### Airwallex SG

| 항목 | 내용 |
|---|---|
| 라운드 수 | 4-5 (Recruiter → HM → Tech 2-3 → Bar Raiser) |
| 일정 | 33일 평균 |
| 코딩 난이도 | LC Medium |
| 시스템 디자인 | 결제 시스템 시나리오 (idempotency, 분산 트랜잭션) |
| 합격 만족도 | 27.7% positive (떨어지는 사람 多) |
| 본인 어필 | Go + K8s + Cloud Platform |
| 보상 | Senior 1.94-2.3억 (median 185K SGD) |

**자주 나오는 SD**:
- Design a global payments processing system
- Design idempotent payment retry
- Design FX rate distribution

**팁**: Bar Raiser 까다로움. 본인 trade-off 명확하게 설명 못하면 fail.

---

### OKX SG

| 항목 | 내용 |
|---|---|
| 라운드 수 | 3-4 (Tech → SD → Manager → HR) |
| 일정 | 2-4주 ⭐ (빠름) |
| 코딩 난이도 | LC Medium + 일부 Hard |
| 시스템 디자인 | 거래 시스템 / 분산 시스템 |
| 직급 | P6.1 Senior: SGD 140-180K / P7.1 Staff: SGD 200-250K |
| 본인 어필 | LLM serving + K8s |
| 컬쳐 | 빠른 결정, 정치적 (Glassdoor) |

**자주 나오는 SD**:
- Design a crypto exchange order matching engine
- Design real-time price feed distribution

**팁**: 첫 영어 인터뷰 워밍업 용도. 빠르고 합격해도 OK 거절도 OK.

---

### Grab SG

| 항목 | 내용 |
|---|---|
| 라운드 수 | 5 (Codility OA + HR + Eng×2 + HM) |
| 일정 | 2-6주 |
| 코딩 난이도 | LC Medium 중심 |
| 시스템 디자인 | 1시간 (Payment, Ride matching) |
| 본인 어필 | Senior ML Eng Simulation은 Scala 관문 ⚠ |
| 보상 | G5 Senior median SGD 255K (2.7억) ⭐ |
| 한국인 친화 | ⭐⭐⭐⭐⭐ 많음 |

**팁**: Grab Simulation 자리는 Scala 필수. Scala 안 하면 AI Platform Architect / Lead ML Foundation Models 다른 자리 고려.

---

### FriendliAI Seoul

| 항목 | 내용 |
|---|---|
| 라운드 수 | 4-5 |
| 코딩 난이도 | LC Medium + GPU/CUDA 기본 (도메인에 따라) |
| 시스템 디자인 | LLM serving 인프라 |
| 영어 환경 | 영어 인터뷰 (글로벌 회사) |
| 본인 어필 | LLMInferenceService 직접 매칭 |
| 보상 | Senior 1.3-1.6억 (한국 스타트업 수준) |

**팁**: LLM serving 도메인 깊이 있으면 본인 정확 매칭. SF transfer 옵션 있음.

---

## 🥉 Step 1 — 연습 카드

### AISG (NUS)

| 항목 | 내용 |
|---|---|
| 라운드 수 | 3-4 (정부 산하라 천천히) |
| 일정 | 1-3개월 |
| 코딩 난이도 | LC Easy-Medium |
| 시스템 디자인 | MLOps 파이프라인 (가벼움) |
| 영어 환경 | 100% 영어, 부담 적당 |
| 본인 어필 | MLOps Platform 빌드 직접 매칭 |
| 보상 | SGD 90-140K (0.95-1.5억, 미달) |

**팁**: 영어 인터뷰 연습용 최적. 떨어져도/거절해도 OK.

---

### GovTech SG

| 항목 | 내용 |
|---|---|
| 라운드 수 | 3-5 |
| 일정 | 4-8주 |
| 코딩 난이도 | LC Medium |
| 시스템 디자인 | Public sector 시나리오 |
| 보상 | SGD 110-160K (1.2-1.7억) |

**팁**: AISG와 비슷. 연습용 카드.

---

## 📊 인터뷰 강도 비교표

```
회사            라운드  코딩       SD     Behavioral  영어부담  보상(Senior)
─────────────────────────────────────────────────────────────────────────
TikTok/BD SG    4-6    Medium-Hard  ★★★    ★★         ★★★       2.1-3.5억
Apple SG        4-5    Medium       ★★     ★★★        ★★★       2.1-3.5억
Anthropic Tokyo 5-6    Medium-Hard  ★★★    ★★★        ★★★       4.2-7억
Airwallex SG    4-5    Medium       ★★★    ★★         ★★        1.94-2.3억
OKX SG          3-4    Medium-Hard  ★★     ★          ★★        1.5-2.1억
Grab SG         5      Medium       ★★     ★★         ★★        2.7억
FriendliAI KR   4-5    Medium       ★★     ★          ★         1.3-1.6억
AISG (연습)     3-4    Easy-Medium  ★      ★          ★★        0.95-1.5억
GovTech SG      3-5    Medium       ★★     ★          ★★        1.2-1.7억
```

---

## 🎯 매일 체크리스트

```
□ LC 1문제 (medium)
□ 영어 자기소개 3분 1회 (녹음)
□ STAR 답변 1개 외우기 (10개 로테이션)
□ SD 주제 1개 영어로 5분 설명 (녹음)
□ 회사별 cheatsheet 1번 훑기
```
