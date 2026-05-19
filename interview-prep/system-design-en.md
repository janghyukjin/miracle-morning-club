# System Design — English Answer Guide

본인 강점 (K8s/MLOps/LLM Serving)을 영어로 설명하는 패턴 가이드.

---

## 🎯 표준 시스템 디자인 답변 프레임 (45분 인터뷰 기준)

| 단계 | 시간 | 영어 패턴 |
|---|---|---|
| 1. Requirements clarification | 5-7분 | "Before I jump in, let me clarify the requirements..." |
| 2. Capacity estimation | 3-5분 | "Let's estimate the scale we're designing for..." |
| 3. High-level design | 10-15분 | "Here's my proposed architecture at a high level..." |
| 4. Deep dive | 10-15분 | "Let me deep dive into the [X] component..." |
| 5. Trade-offs & follow-up | 5분 | "There's a key trade-off here between A and B..." |

---

## 🗣️ 단계별 영어 표현 패턴

### 1. Requirements Clarification

```
"Before I jump into the design, I'd like to clarify a few requirements."

"Are we designing for [X] users? What's the read-to-write ratio?"

"What's the SLO for latency? Are we optimizing for throughput or latency?"

"Are there any specific consistency requirements — strong, eventual, or read-your-writes?"

"Is geographic distribution in scope? Single region or multi-region?"

"What's the budget for cost? Are we optimizing for compute cost or storage cost?"
```

### 2. Capacity Estimation

```
"Let me do a quick back-of-envelope calculation."

"Assuming [X] DAU with [Y] requests per user per day, that's roughly [Z] RPS."

"For storage, if each record is about [N] KB and we have [M] records, total storage is approximately [P] TB."

"Peak traffic is typically 3 to 5 times average, so we should design for [peak] RPS."
```

### 3. High-Level Design

```
"At a high level, the architecture has [N] main components."

"Client requests come in through a load balancer, hit our API gateway, then route to the [X] service."

"The [Y] service is the core component — it handles [responsibilities]."

"For data persistence, I'd use [DB choice] because of [reason: write throughput / read latency / consistency]."

"For caching, [Redis / Memcached] with [LRU / LFU] eviction policy."
```

### 4. Deep Dive

```
"Let me zoom into the [X] component."

"The key challenge here is [problem]. There are a few approaches..."

"Approach A is [option]. Pros are [P]. Cons are [C]."

"I'd lean toward Approach B because [trade-off reasoning]."

"For scaling, we shard by [key] — this gives us [property: locality / hot-key avoidance]."
```

### 5. Trade-offs

```
"Let me call out a few key trade-offs in this design."

"We chose [X] over [Y] because [reason], but the trade-off is [downside]."

"If [scenario], we'd need to evolve this to [alternative]."

"Areas I haven't covered but are important: [security / observability / disaster recovery]."
```

---

## 🔥 본인 도메인별 자주 나오는 SD 문제 + 답변 패턴

### Q1. "Design a model serving platform" (TikTok / ByteDance / Anthropic 자주)

**본인 강점**: LLMInferenceService 직접 개발

**답변 골격**:
```
1. Clarify:
   - Online inference vs batch?
   - Latency SLO (p50, p99)?
   - Multi-model or single-model?
   - GPU availability — homogeneous or heterogeneous?

2. Estimate:
   - QPS per model
   - Token throughput
   - GPU memory required (model size + KV cache)

3. High-level:
   - API Gateway (auth, rate limiting via Envoy/Istio)
   - Model router (multi-model dispatch)
   - Inference workers (vLLM, TensorRT-LLM, Triton)
   - Autoscaler (KEDA / custom HPA)
   - Model registry (S3 + metadata DB)

4. Deep dive — Inference workers:
   - Batching strategy (continuous batching, dynamic batching)
   - KV cache management
   - Multi-node inference (tensor parallelism, pipeline parallelism)
   - Speculative decoding for latency

5. Trade-offs:
   - Throughput vs latency (large batch = high throughput, high latency)
   - Cost vs performance (quantization trade-off)
   - Reliability (warm pool vs cold start for autoscaling)
```

**본인 차별화 포인트**:
- "At NAVER, I built LLMInferenceService with **GroupDisruptionBudget** CRD to handle multi-node group lifecycle — standard PodDisruptionBudget doesn't work for multi-node."
- "We use **PriorityClass + ExtendedResource** for GPU quota, not standard ResourceQuota — because of GPU heterogeneity."

---

### Q2. "Design a Kubernetes-based platform for X" (Airwallex / OKX / 일반 SaaS)

**본인 강점**: mlx-operator main contributor

**답변 골격**:
```
1. Clarify:
   - What kind of workloads? Stateful or stateless?
   - Multi-tenancy required?
   - Self-service or admin-only?

2. Architecture:
   - Custom CRD for workload abstraction
   - Operator (controller + webhook) for reconciliation
   - API server for user-facing API
   - Resource quota system (per workspace / project)

3. Deep dive — Operator pattern:
   - Reconciliation loop
   - Status conditions (Cluster-API pattern)
   - Admission webhook for validation
   - Finalizer for cleanup

4. Multi-tenancy:
   - Namespace isolation
   - NetworkPolicy
   - PriorityClass per tier
   - ResourceQuota per tenant

5. Trade-offs:
   - CRD vs ConfigMap (typed API vs flexibility)
   - Operator vs scheduled job (event-driven vs periodic)
   - Sync vs async API (latency vs reliability)
```

**본인 차별화**:
- "I designed Zone, ManagementQuota, ProjectExtraQuota CRDs at NAVER MLX — established Operator pattern conventions across the team."
- "I solved a real memory leak from managedFields accumulation."

---

### Q3. "Design a real-time messaging / event system" (Stripe / Airwallex / Grab)

**본인 강점**: NATS 클러스터 운영 + Executor (gRPC routing)

**답변 골격**:
```
1. Clarify: at-least-once vs exactly-once? Ordering?
2. Components: Producer → Broker (NATS/Kafka) → Consumer
3. Deep dive: partitioning, consumer groups, backpressure
4. Operations: monitoring (NATS JetStream consumer lag)
5. Trade-offs: NATS (low latency, simpler) vs Kafka (high throughput, complex)
```

**본인 차별화**:
- "I operated NATS clusters across private/public/neuro networks at NAVER."
- "I resolved gRPC routing issues including SSE event TCP boundary corruption — fixed via Content-Type-based buffering."

---

## 💡 영어 SD 인터뷰 핵심 팁

### 1. Think Out Loud
한국인이 가장 어려워하는 부분. 속으로 설계하지 말고 **계속 말로**:
```
"Hmm, let me think about this..."
"One option is X, but I'm worried about [problem]..."
"Actually, let me reconsider — what if we [alternative]?"
```

### 2. Diagram Driving
보드/태블릿 사용 가능하면 **그림 그리면서 설명**. 영어 말이 막힐 때 다이어그램이 backup.

### 3. Ask Permission to Dive Deeper
```
"Would you like me to deep dive into the inference worker, or move on to the scaling strategy?"
```

### 4. Pre-empt Follow-ups
면접관이 follow-up 하기 전에 본인이 먼저:
```
"You might ask about cold start latency — let me address that..."
"This design has a single point of failure at X — let me discuss the HA strategy..."
```

### 5. Acknowledge Limitations
모르면 솔직히. 단 우물쭈물 X:
```
"I haven't worked with that specifically, but based on first principles I'd approach it as..."
"I'd need to research [X] more, but here's my initial intuition..."
```

---

## 📚 추천 학습 자료

| 자료 | 우선순위 |
|---|---|
| **Designing Data-Intensive Applications** (Kleppmann) | ⭐⭐⭐⭐⭐ 필독 |
| **System Design Interview Vol 1/2** (Alex Xu) | ⭐⭐⭐⭐ |
| ByteByteGo (YouTube) | ⭐⭐⭐⭐ 영어 표현 패턴 |
| Tech Dummies (YouTube) | ⭐⭐⭐ |
| NVIDIA / vLLM / TensorRT-LLM 블로그 | ⭐⭐⭐⭐⭐ 본인 도메인 |
| KServe / Kubeflow 공식 문서 | ⭐⭐⭐⭐ |

---

## 🎬 매일 루틴 권장

1. SD 주제 1개 선정 (예: "Design Twitter timeline")
2. 5분 자료 안 보고 영어로 설명 → 녹음
3. 재생하면서 막힌 부분 / fillers 체크
4. 5분 표준 답안 학습 → 다시 5분 영어로 설명
5. 주 5회, 8주 완성 권장
