# Agent Protocol

This repository is deliberately model- and interface-neutral. ChatGPT, Claude, Codex, Hermes, local models, and humans should be able to participate through the same research contract.

## Route by session intent

Before writing research artifacts, classify the interval:

- **learning** — learner capability/mental-model change -> study checkpoint / evidence;
- **lab development** — Open Learning Lab architecture, governance, tooling, protocol, or operations -> Issue / ADR / PR;
- **mixed** — split the records and cross-link them.

Do not treat project-development activity as learner evidence merely because it occurred in a learning-related conversation.

## Before acting

1. Read `CHARTER.md`.
2. Identify the learner goal and active hypothesis.
3. Distinguish current evidence from interpretation.
4. Retrieve current external sources when the learning domain is active or time-sensitive.
5. Do not promote an observation to a finding without the evaluation specified by the experiment.

## Agent roles

Roles are functions, not persistent personas:

- **Researcher** — retrieves current sources and provenance.
- **Tutor** — chooses a learning action under the active policy.
- **Evaluator** — administers unassisted tests and records evidence.
- **Coordinator** — routes uncertain, high-value questions to sources or experts and synthesizes without erasing disagreement.

One agent may perform several roles, but should preserve their separation in the record.

## Write contract

Agents may propose:

- hypotheses through Issues;
- experiments through PRs;
- observations/evidence through ledger additions;
- findings only when linked to evidence;
- corrections by adding a superseding record.

Never overwrite a published result merely because a later result disagrees.

## Expert input

Do not average expert opinions into consensus. Preserve:

- target claim;
- judgment;
- rationale;
- expertise context;
- confidence if provided;
- provenance;
- later outcome/calibration when available.

## Learner privacy

Do not commit raw private transcripts, hidden profile data, medical/financial information, credentials, or unrelated personal context. Publish the minimum learner-authored excerpt or structured observation needed for the experiment, with explicit provenance and consent.

## Learning policy

Prefer actions that generate decision-relevant evidence:

`explain | ask | challenge | retrieve | reconstruct | transfer | visualize | withhold-help | route-to-expert`

The tutoring agent must not grade its own success from conversational fluency. Use learner behavior.

## Current study

See `studies/marin/README.md` and `ledger/experiments/E001.json`.
