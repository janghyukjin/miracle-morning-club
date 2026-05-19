# JD-CV Gap & 우회 답변 패턴

각 타겟 공고의 요구사항 vs 본인 CV 갭 + **갭을 인정하면서 본인 강점으로 우회**하는 영어 답변 패턴.

---

## 🔑 우회 답변 공통 프레임 (외워두기)

```
Pattern 1 — "Adjacent experience":
  "I haven't worked with X directly, but I have built Y at NAVER which solves
   a similar class of problems. Specifically, [본인 경험 디테일]. So I'm confident
   I can ramp up on X quickly because the underlying principles are the same."

Pattern 2 — "First principles":
  "I don't have hands-on with X, but based on first principles, I'd approach it
   by [본인 추론]. At NAVER I made a similar reasoning when [본인 경험], where
   I [구체 행동]."

Pattern 3 — "Learning trajectory":
  "X is on my reading list — I've gone through [paper/blog/docs]. The core
   trade-off I see is [본인 이해]. I'd want to validate this hands-on early
   in the role."
```

---

## 1️⃣ TikTok Tech Expert - LLM Model Serving ⭐ 1순위

### JD 핵심 요구사항

```
✅ 대규모 ML 모델 deployment (3+ years)
✅ Python / C++ / Golang
✅ TensorFlow, PyTorch, DeepSpeed
⚠ quantization, distillation, distributed inference, ONNX, ZeRO
✅ RPC, Redis, Kafka
```

### Gap 분석

| 항목 | 본인 매칭 | Gap |
|---|---|---|
| 대규모 ML deployment | ✅ LLMInferenceService 직접 | — |
| Go / Python | ✅ 강함 | — |
| Distributed inference | ✅ multinode inference 직접 | — |
| RPC / Redis / Kafka | ✅ gRPC, NATS, VictoriaMetrics | Kafka는 X (NATS 인접) |
| **DeepSpeed / ZeRO** | ❌ 직접 X | ⚠ 학습 인프라 측면 |
| **Quantization / Distillation** | ❌ 모델 압축 직접 X | ⚠ 서빙만 |
| **ONNX** | ❌ TensorRT/Triton 우회 | ⚠ |
| **C++** | ❌ 약함 | ⚠ 옵션 (Go/Python/C++ 택1) |

### 🎤 우회 답변 패턴

**Q: "Tell me your experience with DeepSpeed / ZeRO."**
```
"To be transparent, I haven't worked with DeepSpeed in production directly —
my work has been on the serving side, not training infrastructure.

That said, I've studied DeepSpeed's ZeRO partitioning strategies and how they
relate to inference parallelism. At NAVER, my LLMInferenceService work
involves tensor parallelism and pipeline parallelism for multi-node inference,
which shares many concepts — sharding state across GPUs, communication patterns
via NCCL, KV cache management.

If I joined this team, I'd want to ramp up on DeepSpeed's specifics quickly
because the underlying distributed systems principles are familiar to me."
```

**Q: "Have you done model quantization or distillation?"**
```
"I haven't optimized models directly — that's typically the modeling team's
work at NAVER. But on the serving side, I've worked with quantized models
deployed through our platform — INT8 and FP16 variants — and I understand
the trade-offs in latency, accuracy, and GPU memory footprint.

I'd be excited to learn the hands-on side of quantization in this role, since
serving optimization and model optimization are increasingly merged."
```

**Q: "Why do you want to switch from infrastructure to model serving?"**
```
"I'm not switching — I'm doubling down. My core work at NAVER IS LLM model
serving. LLMInferenceService and multi-node inference are exactly this domain.

What I'm looking for is scale. NAVER serves HyperCLOVA X internally.
TikTok serves LLMs to over a billion users. The class of problems
at that scale — latency tails, cost optimization, multi-region serving —
is what I want to work on next."
```

---

## 2️⃣ TikTok SWE - AI Large Model Platform

### JD 핵심 요구사항

```
✅ Bachelor's degree + (years not strict)
✅ Distributed systems
✅ Go / Python
⚠ prompt engineering, RAG, MCP, Agent architecture, LLM deployment
✅ AI/ML system realities
```

### Gap 분석

| 항목 | 본인 매칭 | Gap |
|---|---|---|
| 분산 시스템 | ✅ mlx-operator, multinode | — |
| Go / Python | ✅ | — |
| LLM deployment | ✅ LLMInferenceService | — |
| **Prompt engineering** | ⚠ 인프라 측면만 | 모델 사용 측면 X |
| **RAG** | ❌ 직접 구축 X | 인프라 지원만 |
| **MCP, Agent architecture** | ❌ 직접 X | ⚠ |

### 🎤 우회 답변 패턴

**Q: "Tell me about your experience with RAG or Agent systems."**
```
"My direct experience is on the infrastructure side — I've enabled RAG and
agent workloads on NAVER's MLX platform by providing the multi-node inference,
vector DB integration patterns, and request routing.

I haven't been the one building the agent logic or RAG retriever, but I've
worked closely with the modeling teams to understand their requirements
— for example, the latency budget for a multi-step agent, or the throughput
requirements for embedding generation.

In this role, I'd want to extend my experience into the agent application
layer, especially because the infra design is shaped by what agents need."
```

**Q: "What's your take on MCP (Model Context Protocol)?"**
```
"I've read the MCP spec and understand it's an emerging standard for connecting
LLMs to external context sources. I see it as a protocol-level abstraction
similar to gRPC for AI workloads — separating model logic from context retrieval.

From an infrastructure perspective, MCP creates new challenges: caching
context, security boundaries, latency budgeting across hops. These are
problems I've solved at NAVER for similar request-routing patterns —
my Executor component handles this kind of multi-step routing.

I'd be excited to apply that thinking to MCP."
```

---

## 3️⃣ ByteDance SWE - AI Infrastructure

### JD 핵심 요구사항

```
✅ Go / Python / Java / Node.js / Rust / C
✅ Large-scale distributed systems
✅ Kubernetes
⚠ Knative, Firecracker, serverless platforms (AWS Lambda 등)
✅ Containerization, networking, distributed tracing
```

### Gap 분석

| 항목 | 본인 매칭 | Gap |
|---|---|---|
| Go | ✅ 강함 | — |
| 분산 시스템 | ✅ mlx-operator + multinode | — |
| K8s | ✅ 마스터 | — |
| **Knative** | △ 알고 있지만 production X | ⚠ |
| **Firecracker** | ❌ 직접 X | ⚠ microVM |
| **Serverless platforms** | ❌ 운영 X (구축은 인접) | ⚠ |
| Containerization | ✅ 운영 | — |
| Distributed tracing | ✅ Tempo + OTLP | — |

### 🎤 우회 답변 패턴

**Q: "Have you worked with Knative or built serverless?"**
```
"I haven't run Knative in production, but I'm very familiar with its concepts —
auto-scaling to zero, request-driven scaling, cold start handling.

At NAVER, I designed our autoscaling controller and CLOpsDeployment CRD,
which solves similar problems for ML serving — scaling based on inference
request load, managing pod lifecycle. We didn't use Knative directly because
of GPU scheduling requirements, but the design principles are the same.

I'd ramp up on Knative quickly because the patterns are familiar."
```

**Q: "What about Firecracker / microVMs?"**
```
"I haven't operated Firecracker in production, but I understand the use case —
strong isolation with VM-like security but container-like startup time, for
multi-tenant serverless workloads.

My closest experience is the LINE Verda Operator — I managed 40,000 VMs
across DBaaS workloads. Different scale of isolation, but similar problems:
provisioning latency, lifecycle management, resource limits, security boundaries.

I'd be interested in working with Firecracker specifically because the cold
start problem at AI serving scale is something I've thought about a lot."
```

---

## 4️⃣ Airwallex Senior SWE, Cloud Platform

### JD 핵심 요구사항

```
✅ 5+ years (2+ years platform/infra) — 본인 정확 매칭
✅ Go / Python / Java
⚠ GCP (primary) — 본인은 NCP/AWS 위주
✅ Data pipeline + large datasets
⚠ IAM, RBAC/ABAC, secrets management (security 중심)
⚠ HashiCorp Vault, GitLab CI/CD
✅ Kubernetes resource management
도메인: Cost & Billing Platform + Security & Access Platform (JIT)
```

### Gap 분석

| 항목 | 본인 매칭 | Gap |
|---|---|---|
| Go | ✅ 강함 | — |
| K8s resource management | ✅ Quota/Priority 마스터 | — |
| **GCP** | △ AWS는 일부, NCP 위주 | ⚠ 학습 가능 |
| **Cost & Billing** | ❌ 새 도메인 | ⚠ |
| **IAM / RBAC / JIT** | △ K8s RBAC만, IAM JIT X | ⚠ |
| **HashiCorp Vault** | ❌ 직접 X | ⚠ |
| GitLab CI/CD | △ GitHub Actions 위주 | 인접 |

### 🎤 우회 답변 패턴

**Q: "Have you built a cost attribution / billing pipeline?"**
```
"I haven't built a billing pipeline directly. My closest experience is
the GPU quota and resource attribution work at NAVER — I designed the
PriorityClass and ExtendedResource-based ResourceQuota system that tracks
allocation and usage per workspace and project.

The core problems are similar: ingesting usage data, attributing it to
the right cost center, exposing reporting APIs, building anomaly detection.

What's new for me here would be the billing-specific concepts — currency
conversion, tax handling, GCP-specific data formats. But the platform
engineering side is exactly what I've been doing."
```

**Q: "Tell me about your IAM / JIT access experience."**
```
"I've worked extensively with Kubernetes RBAC and admission webhooks — for
example, I designed admission validation for ManagementQuota and ratelimit
control. I understand RBAC well from the K8s side.

I haven't built a JIT IAM system specifically. But I understand the
motivation — replacing standing privileges with time-bound, request-driven
access reduces blast radius.

If I joined, I'd want to learn HashiCorp Vault and the broader IAM/JIT
patterns. Coming from the K8s RBAC and admission webhook side, I have
the policy-as-code mindset, just applied to a different layer."
```

---

## 5️⃣ OKX Senior/Staff Engineer, AI Agent

### JD 핵심 요구사항

```
✅ 5+ years
✅ Distributed systems / large-scale
⚠ AI Agent development (LLM tool use, function calling, agent loops)
⚠ Crypto domain knowledge (helpful)
✅ Backend (Go/Python typical)
```

### Gap 분석

| 항목 | 본인 매칭 | Gap |
|---|---|---|
| 분산 시스템 | ✅ | — |
| Backend (Go/Python) | ✅ | — |
| LLM 인프라 | ✅ LLMInferenceService | — |
| **AI Agent 개발** | ❌ Agent application X | ⚠ |
| **Function calling** | ❌ 직접 X | ⚠ |
| **Crypto 도메인** | ❌ X | △ |

### 🎤 우회 답변 패턴

**Q: "What's your experience with building AI Agents?"**
```
"I've enabled agent workloads on NAVER's MLX platform from the infrastructure
side — providing the multi-node serving, tool-calling latency optimization,
and request routing patterns.

I haven't built an agent application end-to-end, but I've worked closely
with teams building agentic systems internally. I understand the typical
architecture — orchestrator, tool registry, memory/context store,
LLM inference layer.

In this role, I'd extend from the infra layer up into the agent application
layer. My background in CRD design and operator patterns translates well
to managing agent lifecycles."
```

**Q: "Do you have crypto domain knowledge?"**
```
"I don't have professional crypto domain experience. I've been a user of
crypto exchanges and have a basic understanding of order books, futures,
spot trading.

What I bring is platform engineering experience that translates across
domains — handling high-throughput, low-latency systems with strong
consistency. The crypto domain knowledge I'd ramp up quickly through the
team and product."
```

---

## 🎯 공통 갭 → 우회 핵심 메시지

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ "I haven't built X, but I've built Y at NAVER which solves the same class of         │
│  problems. The fundamentals translate, and I'd ramp up quickly."                     │
│                                                                                      │
│ "I'm transparent about gaps but confident in my underlying engineering principles.   │
│  I'd validate my approach hands-on early in the role."                                │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

## 📋 갭 답변 5가지 핵심 원칙

1. **인정하되 사과하지 않기** — "I haven't done X" OK, "I'm sorry I don't know X" ❌
2. **본인 강점으로 즉시 연결** — gap → bridge to strength within 10 seconds
3. **First principles 추론** — "Based on the problem, I'd approach..."
4. **학습 의지 명시** — "On my reading list", "I'd validate hands-on"
5. **본인 임팩트 끼워넣기** — mlx-operator memory leak / LLMInferenceService / Verda Operator 같은 구체 예시
