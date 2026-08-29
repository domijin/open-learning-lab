# Architecture

## Three planes

### 1. Learning plane
The learner interacts through any convenient interface: ChatGPT, Claude, voice, Codex, web UI, or a human mentor.

Properties: fast, adaptive, conversational, partly private.

### 2. Research plane
The Git repository stores canonical public research objects and provenance.

Properties: reviewable, structured, append-oriented, agent-readable.

### 3. Community plane
Issues, PRs, reviews, forks, and later optional forums/Discord/email support public challenge and replication.

Properties: asynchronous, plural, heterogeneous.

GitHub is **not** the learner database, and chat transcripts are **not** the canonical research record.

## Canonical object graph

```text
LearningGoal
    |
    +--> Hypothesis
           |
           v
       Experiment
        /      \
Observation  Evidence
        \      /
         Finding
            |
         Decision
```

Expert judgments may target any claim, experiment, evidence item, or finding.

## Agent-neutral boundary

Agents read repository state and emit the same objects. Vendor-specific prompts/adapters may exist later, but canonical semantics live in schemas and protocols.

## Public/private split

Public:
- learning goals that the learner chooses to publish;
- hypotheses and experiments;
- selected evidence and evaluation results;
- expert judgments;
- findings/decisions;
- source provenance.

Private/local by default:
- raw conversations;
- detailed learner profile;
- unrelated personal context;
- sensitive data;
- private expert communication until consented.

## Why no backend yet

The v0 workflow is chat + GitHub. A custom service earns its existence only when we observe repeated friction that cannot be handled reliably by files, Issues, PRs, or lightweight scripts.

## Future components (hypotheses, not requirements)

- learner dashboard;
- private learner-state store;
- expert review UI;
- cross-agent API/MCP;
- evidence graph/query layer;
- adaptive retrieval scheduler;
- generated public site;
- contextual expert calibration.
