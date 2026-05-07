# 🌅 미라클 모닝 클럽

> 6개월 알고리즘 + 영어 마스터 로드맵 — 매일 한 걸음씩, 함께

🌐 **Live**: https://janghyukjin.github.io/miracle-morning-club/

## 📋 구성

| 페이지 | 설명 |
|---|---|
| `index.html` | 메인 로드맵 (가이드라인, 문제집, Phase, 함께하기) |
| `checklist.html` | 개인 진도 체크리스트 (localStorage 저장) |
| `solutions/` | 풀이 공유 폴더 (각자 본인 폴더에 push) |

## 🎯 핵심 기능

### 1. 개인 진도 체크리스트
- localStorage 기반, 브라우저 단위 저장
- 시작일(5/8) 기준 **현재 주차 자동 감지**
- 26주 캘린더 히트맵 + Phase별 진행률
- streak 카운터 + 데이터 export/import

### 2. 출석보드 (GitHub 잔디)
- repo에 commit하면 자동 출석
- 메인 페이지 "함께하기" 섹션에 최근 30일 활동 표시
- 누가 뭐 올렸는지 commit 히스토리에 자동 누적

### 3. 풀이 공유
- `solutions/[username]/week-XX/` 구조
- 각자 push → GitHub 자연스러운 협업
- 다른 멤버 풀이 참고 가능

## 🚀 클럽 참여하기

1. **collaborator 초대 요청** (관리자에게)
2. clone:
   ```bash
   git clone https://github.com/janghyukjin/miracle-morning-club.git
   ```
3. 본인 폴더 생성: `solutions/[username]/`
4. 매일 push → 자동 출석

자세한 풀이 push 가이드는 [`solutions/README.md`](./solutions/README.md) 참고.

## 🗓️ 일정

- **시작**: 2026-05-08 (목)
- **종료 목표**: 2026-11-08 (26주)
- **주간 시간**: 11h (평일 5h + 주말 집중일 5-6h)
- **주말 집중일**: 토 또는 일 중 본인 선택

## 📚 커리큘럼

- **메인**: NeetCode 150 완주 (Week 1-20)
- **Phase 4**: 회사 태그 (LC Premium) 50-100문제 추가
- **약점 영역**: NeetCode 250에서 보강

## 4단계 Phase

| Phase | 기간 | 주제 |
|---|---|---|
| 1 | Week 1-4 | 기반 다지기 |
| 2 | Week 5-12 | 패턴 마스터 |
| 3 | Week 13-20 | Hard + System Design |
| 4 | Week 21-26 | 인터뷰 준비 + 지원 |

## 📜 라이선스
Personal study repo.
