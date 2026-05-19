# Elevator Pitch — Hyukjin Jang

영어 자기소개 3가지 길이 버전. **소리 내서 100번 반복** 권장.

---

## 🎤 30초 버전 (recruiter 첫 콜 / "Tell me about yourself" 짧은 답)

> Hi, I'm Hyukjin. I'm an MLOps Engineer at NAVER Cloud with five and a half years of experience. I'm the main contributor of mlx-operator, NAVER's Kubernetes-based ML platform, and the sole owner of LLMInferenceService for multi-node LLM serving. Before NAVER, I worked at LINE on database-as-a-service, managing five thousand services across forty thousand VMs. I'm interested in this role because [REASON — customize per company].

**연습 포인트**:
- "five and a half years" — 정확히 발음
- "mlx-operator" — "M-L-X operator" 로 끊어서
- "LLMInferenceService" — "L-L-M inference service"
- 마지막 한 줄은 회사별 customize

---

## 🎤 1분 버전 (phone screen 메인 답)

> Hi, I'm Hyukjin Jang. I've been an MLOps Engineer for about five and a half years.
>
> I'm currently at NAVER Cloud, where I build and operate MLX, our internal ML platform serving thousands of researchers and engineers. I'm the **main contributor** of mlx-operator — designing core CRDs like Zone, ManagementQuota, and PriorityClass-based GPU quota. I'm also the **sole owner** of LLMInferenceService, leading the design of multi-node inference for next-generation serving.
>
> Earlier I was at LINE Plus, where I built the MySQL DBaaS on Kubernetes — about five thousand services and ten thousand VMs. I also developed the Verda Operator that managed forty thousand VMs across different database engines.
>
> Beyond engineering, I'm an active speaker — I presented at DAN 25 on large-scale MLOps for GPU efficiency, and at Engineering Day on CLOps, our multi-cluster ML serving platform.
>
> I'm looking for [TARGET ROLE] because I want to apply this experience at a larger global scale.

**연습 포인트**:
- 끊어 읽기: 문장당 **3-5초** 단위
- 강조어: **main contributor / sole owner / forty thousand VMs**
- 마지막 줄 회사별 customize ("at a larger global scale" 같은 generic motivation)

---

## 🎤 3분 버전 (onsite "Walk me through your background")

> Sure, I'd love to walk you through my background.
>
> I started my career at **LINE Plus** in 2021 as a Database Engineer. I operated MySQL and MongoDB for various LINE services, and built monitoring tools for the DBaaS platform. After about nine months, I moved into the Cloud Service Developer role, where I built the **MySQL DBaaS on LINE Private Cloud**. That platform managed around five thousand services and ten thousand VMs in Kubernetes. I also developed the **Verda Operator** — a common VM creation module that supported about forty thousand VMs across different DBMS engines.
>
> [Pause for breath]
>
> In 2023 I joined **NAVER Cloud** as an MLOps Engineer on the MLX platform team. MLX is NAVER's Kubernetes-based ML platform that supports both internal teams and external customers, including HyperCLOVA X — NAVER's large language model.
>
> My biggest contributions are in three areas. First, **mlx-operator** — I'm the main contributor. I designed core CRDs like Zone, ManagementQuota, ProjectExtraQuota, and MachineProfile. I also independently designed the **PriorityClass and ExtendedResource-based ResourceQuota** architecture for public-zone GPU quota control, which became the core quota structure of our platform.
>
> Second, **LLMInferenceService** — I'm currently the sole owner. I'm leading the full architecture design and implementation of multi-node inference, including a new CRD called **GroupDisruptionBudget** for workload lifecycle management across inference groups.
>
> Third, **operations and performance** — I proactively discovered and resolved a memory leak in mlx-operator caused by Kubernetes managedFields accumulation. I also optimized VictoriaMetrics by removing high-cardinality metrics — achieving a sixty-seven percent reduction and seventy percent memory saving.
>
> Beyond engineering, I'm one of the most active speakers in my team. I've spoken at **DAN 25**, NAVER's flagship developer conference, and at **Engineering Day** in both 2024 and 2025. I'm also a contributor to the **HyperCLOVA X Technical Report** published on arXiv.
>
> I'm exploring opportunities at [COMPANY] because [COMPANY-SPECIFIC MOTIVATION].

**연습 포인트**:
- 시간 체크: 정확히 **3분** (180초) 내. 너무 길면 cut
- 자연스러운 호흡 — "Pause for breath" 표시 지점에서 1초 쉼
- 회사별 마지막 문장 미리 준비:
  - TikTok/ByteDance → "your scale of LLM serving is unmatched globally, and I want to build at that scale"
  - Apple → "your privacy-first ML infrastructure approach aligns with my interest in platform reliability"
  - Airwallex → "your engineering-driven culture and IPO trajectory excite me"
  - OKX → "the intersection of AI agents and crypto infrastructure is unique technically"
  - Grab → "Southeast Asia's super-app scale, and the strong Korean engineering community"

---

## 💡 공통 팁

- **속도**: 한국인은 보통 너무 빠름. **slow down by 20%**
- **억양**: 문장 끝을 살짝 올리지 말고 평이하게 내려서 마무리 (확신 있게)
- **fillers 줄이기**: "um", "you know", "kind of" 같은 군더더기 X. 차라리 1초 침묵
- **녹음 → 재생**: 본인 영어 들으면서 발음 교정. 매일 1회 권장
