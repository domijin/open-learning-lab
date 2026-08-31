# CP001 — Sources and Provenance

Retrieval date: **2026-08-31**

Only sources relevant to the Marin learning interval are recorded.

## 1. Marin launch announcement

**Source:** https://marin.community/blog/2025/05/19/announcement/

**Primary-source status:** Marin project site/blog.

**Claims supported:**
- Marin launched as an open lab for transparent foundation-model research/development.
- Experiments were tracked through GitHub issues, PRs, review, execution logs, and issue-level analysis.
- The launch framing emphasized fixed-resource model building, controlled small-scale experiments, scaling laws, negative-result visibility, Speedrun, and Datashop.

**Learner exposure before judgment:** **Yes.** The learner supplied this URL at the start of the study and received an assistant walkthrough before the later judgment-first curriculum. Consequently, later judgments about open development, Speedrun, and scaling are not fully blind to this material.

## 2. Current Marin README on `main`

**Source:** https://github.com/marin-community/marin/blob/main/README.md

**Retrieved blob SHA:** `dc8d5be48e56c1eb76b6aa5a8ca3f4e9c50442b1`

**Claims supported as of retrieval:**
- Marin currently describes itself as a research program, software platform, and community for foundation-model R&D.
- Its core value is explicitly open development, including documentation of processes, experiments, decisions, and failed experiments.
- Current work highlights a frontier mixture-of-experts program and the Delphi scaling suite, which trains across a compute range and uses smaller models to predict larger ones.

**Learner exposure before judgment:** **Partial.** The learner had already seen the general open-development framing and an earlier assistant summary of current model work. The current README's Delphi-centered framing was not presented in the checkpoint interval.

## 3. Marin issue #4918 — archived Speedrun benchmark

**Source:** https://github.com/marin-community/marin/issues/4918

**Primary-source status:** Marin GitHub issue; opened and closed 2026-04-19.

**Claim supported:**
- The issue states that `main` no longer includes the old Speedrun system after #4541 and treats the old Qwen3 Speedrun recipe as a frozen benchmark harness for optimizer comparisons, explicitly not the current official Marin workflow.

**Learner exposure before judgment:** **No.** This source was retrieved during checkpoint capture, after the learner interaction.

## External update for the primary learning session

Earlier tutoring in this interval used the 2025 Speedrun framing as though it were a current project mechanism. The primary learning session should correct this historical/current distinction before using Speedrun as evidence about Marin's present architecture.

This is recorded as an external update only; no new instruction is delivered in checkpoint mode.
