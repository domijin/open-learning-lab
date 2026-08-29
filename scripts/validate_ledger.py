#!/usr/bin/env python3
"""Minimal integrity checks for the public research ledger.

Deliberately uses only the Python standard library. JSON Schemas document the
contract; this script enforces the invariants that matter before merging v0.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "ledger"

PREFIX = {
    "goals": "G",
    "hypotheses": "H",
    "experiments": "E",
    "evidence": "V",
    "findings": "F",
    "decisions": "D",
}

REQUIRED = {
    "goals": {"id", "status", "capability", "success_evidence", "created_at"},
    "hypotheses": {"id", "status", "claim", "falsification", "created_at"},
    "experiments": {"id", "status", "hypotheses", "objective", "protocol", "evaluation", "created_at"},
    "evidence": {"id", "experiment", "target", "kind", "observation", "provenance", "created_at"},
    "findings": {"id", "claim", "evidence", "status", "created_at"},
    "decisions": {"id", "decision", "rationale", "evidence", "created_at"},
}


def load_records():
    records = {}
    errors = []
    for kind, prefix in PREFIX.items():
        folder = LEDGER / kind
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.json")):
            try:
                data = json.loads(path.read_text())
            except Exception as exc:
                errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
                continue
            missing = REQUIRED[kind] - data.keys()
            if missing:
                errors.append(f"{path.relative_to(ROOT)}: missing fields {sorted(missing)}")
            rid = data.get("id", "")
            if not isinstance(rid, str) or not rid.startswith(prefix):
                errors.append(f"{path.relative_to(ROOT)}: id {rid!r} must start with {prefix}")
            if rid in records:
                errors.append(f"duplicate id {rid}: {path.relative_to(ROOT)} and {records[rid][0]}")
            records[rid] = (path.relative_to(ROOT), kind, data)
    return records, errors


def check_links(records):
    errors = []
    for rid, (path, kind, data) in records.items():
        if kind == "experiments":
            for hid in data.get("hypotheses", []):
                if hid not in records or records[hid][1] != "hypotheses":
                    errors.append(f"{path}: unknown hypothesis reference {hid}")
        elif kind == "evidence":
            eid = data.get("experiment")
            if eid not in records or records[eid][1] != "experiments":
                errors.append(f"{path}: unknown experiment reference {eid}")
            target = data.get("target")
            if target not in records:
                errors.append(f"{path}: unknown target reference {target}")
        elif kind == "findings":
            for vid in data.get("evidence", []):
                if vid not in records or records[vid][1] != "evidence":
                    errors.append(f"{path}: unknown evidence reference {vid}")
        elif kind == "decisions":
            for evidence_id in data.get("evidence", []):
                if evidence_id not in records or records[evidence_id][1] != "evidence":
                    errors.append(f"{path}: unknown evidence reference {evidence_id}")
    return errors


def main():
    records, errors = load_records()
    errors.extend(check_links(records))
    if errors:
        print("Ledger validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1
    print(f"Ledger integrity OK: {len(records)} records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
