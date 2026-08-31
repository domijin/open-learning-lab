# ADR-0001 — Separate learning and lab-development timelines

**Status:** Proposed  
**Date:** 2026-08-31

## Context

Open Learning Lab was bootstrapped from a Marin learning conversation. The same conversation later branched into repository architecture, licensing, checkpoint protocol design, and orchestration work.

This created ambiguity: should every branch/checkpoint be interpreted as part of the Marin learning study?

The first checkpoint dry run reinforced the problem. Its failure concerned artifact creation and orchestration integrity, not learner understanding.

## Decision

Maintain two explicit timelines:

1. **Learning timeline** — learner capability, epistemic checkpoints, retrieval/transfer evidence.
2. **Lab-development timeline** — Open Learning Lab architecture, governance, tooling, protocol evolution, and operational failures.

Use learning checkpoint artifacts only for the first. Use Issues, ADRs, design docs, code, and PRs for the second.

Mixed sessions must be split by intent rather than collapsed into one record.

## Consequences

### Positive
- prevents project work from contaminating learning evidence;
- makes protocol failures inspectable as engineering/research-system failures;
- keeps the learner's primary timeline focused;
- gives system-development decisions a conventional reviewable home;
- allows the learning protocol itself to evolve independently.

### Cost
- some events may need cross-links between two timelines;
- contributors/agents must classify interval intent before writing;
- mixed conversations can require two artifacts.

## Example

The conversation that designed Open Learning Lab, checkpoint capture, and licensing is a **lab-development session**, even though it originated from a Marin-learning branch.

The learner's actual Marin judgments/retrieval/transfer remain in the Marin study.

## Follow-up

Agents should use the routing rules in `docs/orchestration.md`.

Future work may add a dedicated development-session capture protocol if normal Issues/ADRs/PRs prove insufficient.
