# Open Learning Lab Orchestration Contract v0.1

**Status:** Proposed / experimental  
**Protocol family:** `oll.orchestration`

## Goal

Allow one agent/interface to hand a learning or lab-development situation to another agent/interface without requiring shared chat history or hidden memory.

The contract is semantic, not transport-specific.

## Design principle

```text
WHAT IS TRUE        WHAT TO DO         WHAT HAPPENED
ContextSnapshot --> HandoffRequest --> HandoffResult
```

Do not collapse these three concerns into one mutable memory object.

---

# 1. ContextSnapshot

A time-bounded, situation-bounded compiled view of the state relevant to a workflow.

Canonical context should be stable for its compilation moment. Recipient-specific disclosure happens in the HandoffRequest.

## Required fields

- `contract_version`
- `context_id`
- `created_at`
- `timeline`
- `situation`
- `state_refs`
- `policy`
- `provenance`

## Timeline

One of:

- `learning`
- `lab-development`

Mixed conversations should produce separate context snapshots or explicitly linked contexts.

## Situation

For a learning context, normally includes references such as:

- study;
- learning goal;
- current checkpoint;
- active experiment;
- active hypotheses.

For lab development:

- project objective;
- issue/ADR/PR references;
- current design decision or failure under investigation.

## State references

Prefer pinned references over copied content.

Each reference should include enough information to retrieve the exact artifact, ideally:

- repository path or URI;
- Git commit/ref;
- semantic ID when available.

Examples:

- `ledger/goals/G001.json@<commit>`
- `studies/marin/checkpoints/CP004/learner-state.md@<commit>`
- evidence IDs `V017`, `V018`

## Freshness

The snapshot creation time says when orchestration state was compiled.

Active-domain source freshness belongs in referenced artifacts or may be summarized with `domain_as_of`.

## Policy

v0.1 keeps policy deliberately small:

- publication/disclosure scope;
- optional policy reference;
- optional expiry.

Do not embed private context merely because the transport supports it.

## Provenance

Record:

- producer interface/agent when known;
- source repository commit;
- parent context/handoff where relevant;
- protocol/prompt version used to compile the snapshot.

No chain-of-thought is required or permitted.

---

# 2. HandoffRequest

A recipient-specific task referencing a ContextSnapshot.

## Required fields

- `contract_version`
- `handoff_id`
- `context_ref`
- `created_at`
- `purpose`
- `recipient_role`
- `objective`
- `required_context`
- `constraints`
- `completion`

## Purpose examples

- `resume-learning`
- `capture-checkpoint`
- `review-checkpoint`
- `evaluate-transfer`
- `expert-review`
- `research-current-domain`
- `lab-design`
- `implement-change`

These are initially open strings; vocabulary should stabilize from observed use.

## Recipient role

Examples:

- tutor;
- evaluator;
- checkpoint-capture;
- researcher;
- expert;
- lab-orchestrator;
- implementer.

Role describes the function, not the model vendor.

## Required context

This is the **projection**.

The HandoffRequest should name the minimum references that this recipient must load from the canonical ContextSnapshot.

Optional context may be listed separately.

## Constraints

Must explicitly carry important behavioral boundaries.

Examples:

- do not continue tutoring;
- use only public study context;
- do not promote findings;
- retrieve current external sources;
- write only to `capture/<study>-<checkpoint>`;
- do not modify prior checkpoint history.

## Completion contract

Specify:

- expected output artifacts;
- success criteria;
- permitted write scope;
- failure behavior.

A handoff that cannot satisfy completion criteria must produce a failed/incomplete HandoffResult rather than a fictional success receipt.

---

# 3. HandoffResult

The durable outcome of one HandoffRequest.

## Required fields

- `contract_version`
- `result_id`
- `handoff_ref`
- `status`
- `completed_at`
- `outputs`
- `verification`

## Status

v0.1:

- `completed`
- `incomplete`
- `failed`
- `input-required`
- `rejected`

Do not overload `completed` to mean "the agent stopped responding."

## Outputs

References to durable artifacts produced.

Examples:

- checkpoint folder;
- evidence IDs;
- PR;
- expert judgment;
- research note;
- updated context snapshot.

Chat text may be summarized but should not be the only critical output.

## Verification

The producing agent should verify:

- required artifacts exist;
- referenced IDs resolve;
- repository validation passed when applicable;
- expected PR/commit exists;
- missing requirements are explicitly listed.

---

# 4. Example — learning session to checkpoint capture

## ContextSnapshot

```yaml
contract_version: oll.orchestration/v0.1
context_id: OC-20260831-001
created_at: 2026-08-31T11:00:00-07:00
timeline: learning

situation:
  study_ref: studies/marin
  goal_ref: G001
  checkpoint_ref: CP004
  experiment_ref: E001
  hypothesis_refs: [H001]

state_refs:
  - ref: studies/marin/checkpoints/CP004/learner-state.md
    commit: abc123
  - ref: ledger/evidence/V017.json
    commit: abc123

domain_as_of: 2026-08-31

policy:
  publication_scope: public-study
  policy_ref: studies/marin/publication-policy.md

provenance:
  repo_commit: abc123
  compiled_by:
    interface: ChatGPT
    model: optional
  parent_context: OC-20260831-000
```

## HandoffRequest

```yaml
contract_version: oll.orchestration/v0.1
handoff_id: OH-20260831-001
context_ref: OC-20260831-001
created_at: 2026-08-31T11:05:00-07:00

purpose: capture-checkpoint
recipient_role: checkpoint-capture

objective: Preserve the epistemic change since CP004 without continuing instruction.

required_context:
  - studies/marin/README.md
  - prompts/checkpoint-capture.md
  - studies/marin/checkpoints/CP004/learner-state.md
  - ledger/experiments/E001.json
  - ledger/hypotheses/H001.json

constraints:
  - do-not-continue-tutoring
  - preserve-verbatim-vs-interpretation
  - no-finding-promotion-without-predefined-evaluation

completion:
  expected_outputs:
    - checkpoint-package
    - verified-capture-pr
  write_scope:
    - capture/marin-CP005
  on_failure: produce-incomplete-result
```

## HandoffResult

```yaml
contract_version: oll.orchestration/v0.1
result_id: OR-20260831-001
handoff_ref: OH-20260831-001
status: completed
completed_at: 2026-08-31T11:15:00-07:00

outputs:
  checkpoint_ref: studies/marin/checkpoints/CP005
  evidence_refs: [V018]
  pr_ref: 42

verification:
  required_artifacts_exist: true
  references_resolve: true
  repo_validation_passed: true
  missing: []
```

---

# 5. Example — checkpoint to lab orchestrator

A different HandoffRequest can reference the same or a related ContextSnapshot but ask the lab orchestrator to review **capture quality**, not teach the subject.

```yaml
purpose: review-checkpoint
recipient_role: lab-orchestrator
objective: Evaluate capture validity and whether the protocol/system should change.

required_context:
  - checkpoint package
  - capture PR
  - checkpoint protocol version
  - active learning hypothesis

constraints:
  - do-not-continue-domain-tutoring
  - separate-orchestration-failure-from-learner-evidence
```

This is the contract boundary for the current Open Learning Lab development thread.

---

# 6. What deliberately does NOT travel in v0.1

- full raw chat transcript;
- hidden model reasoning;
- general personal memory;
- every prior checkpoint;
- complete learner profile;
- vendor-specific conversation/session IDs as semantic requirements;
- arbitrary tool state;
- credentials/secrets.

Agents retrieve deeper context only when the task requires it.

---

# 7. Transport mapping

The semantic contract should work unchanged over:

| Transport | Mapping |
|---|---|
| Git/GitHub | JSON/YAML files + commit refs + PRs |
| MCP | context as Resources; protocol prompts/tools as discoverable capabilities |
| A2A | HandoffRequest maps toward Task; outputs toward Artifacts |
| REST/GraphQL | context/request/result resources |
| Human | rendered Markdown form |

Transport integration is a later experiment.

---

# 8. First falsifiable evaluation

We should not declare v0.1 successful because it looks clean.

Test:

> Can a new agent with no access to the originating conversation resume the correct role and make the correct next decision using only the contract and referenced public artifacts?

Run at least three handoffs:

1. learning session -> checkpoint capture;
2. checkpoint -> lab orchestrator;
3. validated checkpoint -> fresh tutor session.

Measure:

- missing-context requests;
- incorrect role/timeline routing;
- hallucinated state;
- unnecessary context loaded;
- task completion;
- artifact/reference integrity;
- learner-rated continuity after tutor resumption.

A successful contract minimizes both **context failure** and **context bloat**.
