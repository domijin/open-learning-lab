# Research — Orchestration Contract Prior Art

**Status:** Research note  
**Date:** 2026-08-31  
**Question:** What is the smallest portable contract that can move a learning situation between different agents/interfaces without sharing one giant conversation context?

## Executive conclusion

Open Learning Lab should **not invent a monolithic learner-memory blob**.

The strongest prior art points toward three separations:

1. **Situation context vs agent memory** — a portable context should be time-bound, purpose-bound, selective, and provenance-aware.
2. **Task request vs durable output** — communication/instructions should be distinct from artifacts/results.
3. **Event history vs derived state** — historical observations should remain reconstructable while current learner state is a revisable projection.

For v0.1, use three artifacts:

```text
ContextSnapshot
      |
      v
HandoffRequest
      |
      v
HandoffResult
```

Transport is deliberately out of scope. GitHub files work now; MCP, A2A, REST, or another transport can come later.

---

## 1. 1EdTech Trusted Portable Learning Context (TPLC)

Source: https://standards.1edtech.org/publications/rfc-trusted-contextv2

This 2026 public draft is the closest prior art to Open Learning Lab's orchestration problem.

Key principles:

- context is **time-bound** and **situation-bound**;
- it is a **compiled artifact**, not an agent's memory store;
- it should contain enough information for the purpose and no more;
- provenance and policy should travel with context;
- context is transport-agnostic;
- a canonical context can be projected differently for different recipients;
- multi-agent workflows should share a coherent context rather than each agent reconstructing its own view.

### Adopt

- time/situation bounds;
- context as a compiled coordination artifact;
- source/provenance references;
- recipient-specific projection/minimization;
- transport independence;
- explicit purpose.

### Do not adopt yet

- institutional consent machinery;
- signing/verifiable credentials;
- graph infrastructure;
- realtime multi-source service.

Those are valuable later but premature for an N-of-1 public GitHub study.

---

## 2. xAPI

Source: https://github.com/adlnet/xAPI-Spec

xAPI models learning experience statements using:

`Actor + Verb + Object + Result + Context`

and treats statements as durable evidence of experiences.

### Adopt

- learning events should describe **what happened**, not only current state;
- event identity and timestamp;
- result/context/provenance distinction;
- historical records should not be silently rewritten.

### Do not use xAPI as the handoff contract

xAPI is good at recording events but does not answer:

> What does the next tutor/evaluator/researcher need to know and do right now?

Open Learning Lab can later map selected evidence events to xAPI without forcing orchestration semantics into xAPI statements.

---

## 3. 1EdTech Caliper Analytics

Source: https://www.1edtech.org/standards/caliper

Caliper standardizes learning activity/event vocabulary across multiple learning applications and supports cross-tool analytics.

### Adopt

- cross-interface learning events need shared semantics;
- profiles/vocabularies are useful once repeated event types stabilize.

### Defer

Do not define a large event vocabulary before real usage tells us which events recur.

---

## 4. Agent2Agent (A2A)

Source: https://a2a-protocol.org/dev/specification/

A2A 1.0 provides interoperable agent task semantics across opaque agent systems.

Important separation:

- **Messages** communicate;
- **Tasks** represent stateful units of work;
- **Artifacts** are durable outputs;
- agents collaborate without exposing internal reasoning/memory/tool internals.

### Adopt

- task identity;
- explicit lifecycle/status;
- outputs as artifacts rather than relying on transient chat messages;
- opaque-agent assumption;
- capability declaration may become useful later.

### Do not adopt yet

- A2A transport/server implementation;
- network discovery and Agent Cards;
- streaming/push infrastructure.

The Open Learning Lab contract should be compatible in spirit with A2A while remaining usable as plain files.

---

## 5. Model Context Protocol (MCP)

Source: https://modelcontextprotocol.io/specification/2025-11-25

MCP separates resources, prompts, and tools and provides lifecycle/capability negotiation.

### Adopt

Architectural rule:

> The orchestration contract defines **what context and task mean**. MCP may later define **how an agent fetches resources or invokes capabilities**.

Do not embed MCP-specific transport concepts into the semantic contract.

---

## 6. W3C PROV

Source: https://www.w3.org/TR/prov-primer/

PROV distinguishes:

- Entity;
- Activity;
- Agent;
- derivation/association.

### Adopt

Every context/result should be inspectable for:

- what artifacts it came from;
- what activity generated it;
- which human/agent was responsible.

Use lightweight references first rather than implementing PROV serialization.

---

## 7. OpenTelemetry context/baggage

Sources:
- https://opentelemetry.io/docs/specs/otel/context/
- https://opentelemetry.io/docs/concepts/signals/baggage/

OpenTelemetry propagates small execution-scoped context across process boundaries. Baggage is intentionally a lightweight key/value carrier and carries security risks when sensitive information propagates downstream.

### Adopt

Use small correlation identifiers across tools/processes:

- handoff ID;
- study ID;
- checkpoint ID;
- trace/parent ID.

### Reject

Do not put rich learner state or sensitive context into generic transport baggage.

---

## 8. Event sourcing / durable workflow systems

Sources:
- https://martinfowler.com/eaaDev/EventSourcing.html
- https://docs.temporal.io/

Event-sourced systems preserve a durable history from which state can be reconstructed. Durable workflow systems make task progress and failure explicit rather than assuming a side effect succeeded.

### Adopt

- event history is authoritative evidence;
- current learner state is derived/revisable;
- explicit completion/failure states;
- referenced artifacts must be verified before claiming success;
- retries should not fabricate or rewrite history.

The failed CP001 capture is a concrete Open Learning Lab example of why completion semantics matter.

---

# Evaluation criteria for our contract

A useful v0 contract should score well on:

| Criterion | Requirement |
|---|---|
| Portability | ChatGPT, Claude, Codex, humans can interpret it |
| Minimality | Carries only decision-relevant state |
| Replayability | Historical basis can be reconstructed |
| Provenance | Facts/inferences/artifacts have inspectable origins |
| Freshness | Agent can tell when state/source context was compiled |
| Privacy | Context can be projected/minimized by purpose |
| Failure visibility | Missing artifacts cannot masquerade as success |
| Agent opacity | No private chain-of-thought/internal memory required |
| Transport neutrality | Works in Git today; MCP/A2A later |
| Evolvability | Versioned schema and explicit compatibility |

# Recommendation

Define three semantic artifacts:

## A. ContextSnapshot

A canonical, time-bounded description of the current situation.

Answers:

> What is currently true/relevant?

It should mostly contain **references** to authoritative repository artifacts, not copied conversation text.

## B. HandoffRequest

A recipient-specific projection plus task.

Answers:

> Why am I being invoked, what should I do next, what may I read/write, and how will completion be judged?

## C. HandoffResult

A durable completion/failure artifact.

Answers:

> What actually happened, what artifacts were produced, what changed, and what remains unresolved?

This structure can later map naturally to:

- TPLC-like portable context;
- A2A Task/Artifact exchange;
- MCP resource/tool transport;
- xAPI/Caliper event analytics;
- PROV-style provenance.

But v0.1 should remain plain JSON/YAML + Git.


---

## CP001-derived refinements

The first checkpoint dry run and the successful v0.2 recapture provided concrete evidence about the contract design.

### Issue #8 — false completion

**Disposition:** resolved operationally; contract lesson retained.

A capture may not report completion merely because an agent stopped or created one artifact. HandoffResult therefore represents incomplete/failed states explicitly, and a completed result is structurally invalid if required artifacts or references are missing.

### Issue #12 — one-dimensional evidence strength

**Disposition:** valid, but primarily methodology/evidence-schema scope.

The orchestration contract should not treat the project's L0-L5 shorthand as a total ordering of evidence strength. Delay, assistance, transfer distance, novelty/exposure, and authenticity are independent dimensions. The contract transports references; the evidence model defines assessment semantics.

### Issue #13 — replayable provenance

**Disposition:** directly incorporated.

ContextSnapshot now pins the repository/base commit used to compile state, distinguishes protocol path/content hash from repository context, and permits stable source-interval refs with a human-readable fallback.

### Issue #14 — evidence target vs evidential relation

**Disposition:** partially incorporated.

Projected state/evidence refs may carry typed relations such as `diagnostic` or `demonstrates_capability`. This prevents orchestration from implying support merely because an evidence artifact is relevant to an active hypothesis. The canonical ledger schema still needs separate work.

These refinements are evidence-driven changes to the draft contract, not proof that the contract itself is effective.
