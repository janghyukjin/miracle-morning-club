# STAR Answers — Hyukjin Jang

Behavioral 질문 10개. 본인 임팩트 베이스. **각 답변 2-3분 내**.

STAR = **S**ituation · **T**ask · **A**ction · **R**esult

---

## 1️⃣ "Tell me about a challenging technical problem you solved."

**S**: At NAVER, our mlx-operator started showing high memory usage in production, with OOM kills every few days. The platform serves thousands of internal users, so reliability was critical.

**T**: I needed to identify the root cause and fix it without disrupting users.

**A**: I profiled the operator's heap and traced the leak to **Kubernetes managedFields accumulation** — every reconciliation was appending field ownership metadata, growing the object size linearly. I confirmed this by analyzing the etcd object sizes and reproducing in a test cluster. Then I implemented a periodic cleanup of stale managedFields entries and contributed a workaround pattern that the rest of our team adopted.

**R**: Memory usage dropped by about seventy percent, OOM kills eliminated, and we documented the pattern in our team wiki. Other Kubernetes operator teams at NAVER also adopted this approach.

---

## 2️⃣ "Tell me about a time you led a project."

**S**: Our MLX platform needed multi-node inference for next-generation LLMs, but no clear architecture existed across the team.

**T**: As the sole owner, I had to design and lead the entire LLMInferenceService design and implementation.

**A**: I researched existing patterns — KServe, vLLM distributed serving, Triton — and designed a new CRD called **LLMInferenceService**. I also introduced **GroupDisruptionBudget** for workload lifecycle across multi-node groups, since standard PodDisruptionBudget couldn't handle group-level guarantees. I wrote design docs, presented to the team and platform leadership, and coordinated with the inference engine team for integration.

**R**: The design was approved and is currently being rolled out as the next-generation serving capability. I'm continuing to lead the implementation. This is one of the largest architectural changes in the MLX platform.

---

## 3️⃣ "Tell me about a conflict with a colleague."

**S**: When designing GPU quota control for the MLX public zone, another senior engineer proposed using standard Kubernetes ResourceQuota. I believed it wouldn't scale to our GPU heterogeneity (A100, H100, L40S).

**T**: I needed to propose an alternative without dismissing his approach.

**A**: I prototyped my idea — **PriorityClass + ExtendedResource-based ResourceQuota** — over one weekend. I scheduled a 1-on-1, walked him through the prototype, and showed concrete examples where standard ResourceQuota failed. I framed it as "your approach works for v1, mine extends it for v2." We then jointly presented both to the team and the team adopted my design.

**R**: My architecture became the core quota structure of the MLX public zone. The colleague and I have collaborated well since, and we co-authored several follow-up improvements.

---

## 4️⃣ "Tell me about a failure or mistake."

**S**: Early at LINE, I deployed a Verda Operator update that triggered VM re-creation on certain MySQL clusters.

**T**: I had to recover the production state and prevent future occurrences.

**A**: First, I rolled back immediately, then worked with the DBA team to restore data from backup snapshots — affected about 20 services for an hour. Then I did a postmortem: the bug was a missing validation in a webhook that allowed an invalid spec change to trigger re-creation. I added admission validation, integration tests for spec mutation, and a canary deployment policy for operator updates.

**R**: No similar incident recurred for the rest of my time at LINE. The canary policy I introduced is still standard practice for the Verda team. Most importantly, I learned to never trust unit tests alone for operators — admission webhook tests are essential.

---

## 5️⃣ "Why do you want to leave NAVER?"

**S**: I've been at NAVER for about two years and at LINE for three years before that. I built foundational systems at both — mlx-operator, LLMInferenceService, Verda Operator.

**T**: I want to grow at a larger global scale, especially in LLM serving infrastructure.

**A**: I've been exploring opportunities where the scale of inference and the global engineering culture push me further than what's possible within Korea. NAVER has been a great platform for me to build deep expertise, but [COMPANY]'s scale of [SPECIFIC: e.g. "AI Large Model serving"] is unique and aligns with where I want to grow next.

**R**: I'm not running away from NAVER — I'm running toward larger problems. If I join [COMPANY], I want to bring my Operator pattern expertise and LLM serving experience to a global team and contribute at a different scale.

**💡 Tip**: 절대 NAVER 안 좋게 말하지 말 것. "running toward, not away from" 패턴.

---

## 6️⃣ "Tell me about a time you mentored someone."

**S**: New engineers joining the MLX team often weren't familiar with the Kubernetes Operator pattern, which is the foundation of our platform.

**T**: As the main contributor, I needed to onboard them so they could contribute meaningfully within their first three months.

**A**: I wrote a comprehensive Operator pattern guide based on Effective Go principles, presented it as a tech talk to the team, and reviewed every PR from new members for the first month. I also paired with two engineers weekly on their first CRD designs.

**R**: Both engineers became independent contributors within two months — faster than the typical three-month onboarding. The Operator pattern guide became standard team onboarding material, and I was recognized as the most frequent speaker in our team's bi-weekly Tech Talk.

---

## 7️⃣ "Tell me about a time you disagreed with your manager."

**S**: My manager wanted to prioritize a new feature, but I believed we should address technical debt in the rate limiting subsystem first — it was causing intermittent incidents in production.

**T**: I had to advocate for the technical work without coming across as obstructionist.

**A**: I quantified the incident frequency over the past three months (about 2 per week), calculated the engineering hours spent firefighting (about 15% of team capacity), and proposed a two-week focused sprint to refactor. I presented this with the trade-off clearly: "Feature X delivers in week 6 instead of week 4, but team velocity stabilizes."

**R**: My manager agreed. We did the Istio EnvoyFilter-based rate limiting refactor in two weeks. Incident frequency dropped to less than one per month, and we delivered Feature X in week 5 — only one week behind original plan. My manager later mentioned this as an example of "engineer-driven prioritization done right."

---

## 8️⃣ "Tell me about a time you went above and beyond."

**S**: A colleague responsible for NATS clusters across our private, public, and neurocloud networks left the team unexpectedly. No one else was familiar with the system.

**T**: I wasn't asked to take it over, but the platform depended on it.

**A**: I volunteered to absorb the responsibility. I read all his design docs, documented the system end-to-end, resolved all open NATS incidents in neurocloud (timeouts, insufficient storage, peer issues), and built user guides for partner teams. I also rebuilt the message queue's monitoring.

**R**: NATS became one of the most reliable subsystems in our platform — zero incidents for the next six months. I onboarded two partner teams independently. My manager publicly recognized this in our team review.

---

## 9️⃣ "Why this company / role specifically?"

**TikTok Tech Expert LLM Model Serving 버전 예시**:

I'm specifically excited about this role for three reasons.

**First**, the scale. TikTok serves LLMs to over a billion users globally — that's an order of magnitude beyond what I've worked on at NAVER. My LLMInferenceService experience directly translates to challenges at this scale, but the problems are fundamentally different.

**Second**, the technical depth. The role mentions distributed inference, quantization, ZeRO — these are exactly the next problems I want to work on. I've been studying DeepSpeed and vLLM internals on the side, and I want to build at a place where this is the day-to-day work.

**Third**, the team. From reading public engineering blogs and talking to peers, the TikTok inference team has a strong individual contributor culture. I'm not looking to manage — I want to build, and this role explicitly says "Tech Expert" which is the IC track I want.

**💡 Tip**: 회사별 3가지 reason 미리 준비. Scale + Tech depth + Culture/Team 패턴.

---

## 🔟 "Where do you see yourself in 5 years?"

In five years I want to be a **technical leader on global-scale LLM serving infrastructure** — either as a Staff/Principal IC or a small-team Tech Lead.

Concretely: I want to have shipped systems that serve hundreds of millions of users, contributed to open source LLM serving stacks like vLLM or TensorRT-LLM, and spoken at international conferences like KubeCon or MLSys.

What I don't want: managing 30 people away from code, or being a generalist Solutions Architect. I want to stay deep on the inference infrastructure problem.

Joining [COMPANY] is a step toward that — I'll have the scale, the team, and the technical problems that move me along this path.

---

## 💡 공통 팁

- **답변 길이**: 각 1.5-2.5분. 너무 짧으면 detail 부족, 너무 길면 listener 잃음.
- **Result 수치화**: "improved performance" ❌ → "67% reduction in metric series" ✅
- **"I" vs "We"**: 본인 기여는 "I". 팀 작업은 "we, and my specific role was X".
- **NAVER 비판 X**: 5번 질문에서 "running toward, not away from"
- **Follow-up 대비**: 면접관이 "Why didn't X?", "What if Y?" 후속 질문 준비
- **연습**: 거울 보면서 영어로 소리내서. 녹음 → 재생 → 자기 피드백
