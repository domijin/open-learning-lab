# Prompts

Prompts in this directory are **versioned research interventions**, not timeless instructions.

## Checkpoint capture

Use [checkpoint-capture.md](checkpoint-capture.md) from a **conversation branch** created at a meaningful learning checkpoint.

Recommended workflow:

```text
primary learning session
        |
        +--> branch conversation
              |
              v
       run checkpoint-capture
              |
              v
      commit checkpoint + PR
              |
              v
return to primary learning session
```

The capture branch should not continue teaching. Its job is to preserve trace, learner-state interpretation, evidence, sources, and open questions without contaminating the main learning trajectory.

When the prompt changes, update its protocol ID and preserve prior versions in Git history so later analysis can distinguish learning-policy changes from capture-policy changes.
