# Orchestration

Open Learning Lab has **two distinct timelines** that must not be conflated.

## 1. Learning timeline

This is where a learner pursues a real learning objective.

Examples:
- learn Marin;
- learn a scientific topic;
- build capability in a professional domain.

The primary learning conversation should remain uninterrupted whenever possible.

At meaningful epistemic checkpoints, branch the conversation and run the checkpoint-capture protocol.

Artifacts belong under:

`studies/<study>/checkpoints/<checkpoint-id>/`

and, when justified, `ledger/evidence/`.

Learning checkpoints answer:

- What changed in the learner's mental model?
- What capability was demonstrated?
- What remains uncertain?
- What evidence affects an active learning hypothesis?

## 2. Lab-development timeline

This is where contributors build and govern Open Learning Lab itself.

Examples:
- redesign checkpoint capture;
- change repository architecture;
- modify schemas or CI;
- choose licensing;
- improve expert-routing or agent orchestration;
- diagnose a failed capture run.

Artifacts belong in normal project-development surfaces:

- Issues;
- ADRs;
- design docs;
- implementation branches;
- PRs;
- code/tests.

A lab-development event is **not automatically learner evidence**, even if it happens in a conversation that originated from a learning session.

## Why the separation matters

A single conversation may contain both learning and system design, but the repository should preserve the distinction.

```text
LEARNING TIMELINE                       LAB-DEVELOPMENT TIMELINE

learn subject                           build Open Learning Lab
     |                                          |
epistemic checkpoint                     design/ops decision
     |                                          |
capture side branch                      issue / ADR / PR
     |                                          |
study trace + evidence                    code/docs/governance
```

Without this separation, project work can falsely inflate learning evidence, and learning-state interpretation can become polluted by implementation discussion.

## Routing rule

Before recording anything, determine the primary intent of the interval being captured.

### Learning
The dominant question is:
> What did the learner learn, retain, transfer, or misunderstand?

Route to the learning checkpoint protocol.

### Lab development
The dominant question is:
> What should Open Learning Lab build, change, govern, or operationalize?

Route to Issues/ADRs/PRs.

### Mixed interval
Split the record.

Do not force one artifact to represent both purposes. A development decision may reference a learning checkpoint as motivation, while the learning checkpoint may reference a protocol change as context.

## Orchestration failure is project evidence

Failures of the capture machinery—missing files, invalid references, no PR, agent/tool errors—belong to the lab-development timeline.

They may motivate changes to a learning hypothesis only if there is a justified causal connection.

Example:
- CP001 capture created only a manifest and referenced missing V003.
- This is evidence about checkpoint orchestration reliability.
- It is **not** evidence that the learner did or did not understand Marin.

## Current operating model

1. Primary learning threads optimize learning continuity.
2. Checkpoint side branches capture epistemic state without continuing instruction.
3. The Open Learning Lab development thread reviews checkpoint quality, protocol behavior, infrastructure, and governance.
4. Protocol changes are versioned and reviewed through PRs.
5. Failed runs are preserved as project-development evidence rather than cleaned up into success.
