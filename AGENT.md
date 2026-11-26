# AGENT.md — The Absurd Clause Contest

## What this is

An entry for make.fun competition
`u-donrulezz-the-absurd-clause-contest-035cc0f1` ("The Absurd Clause Contest").
`main.py` writes one original absurd terms-of-service clause to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## The entry (177 characters, one sentence, no trailing newline)

> Your subscription, outstanding debts, and unfinished drafts shall, in the
> event of alien abduction, transfer to the abducting party, who shall
> inherit the billing cycle in full.

## How it was chosen

- Field study of all 1,416 submissions in `field-submissions.json`: only 261
  are real clauses; the rest are placeholder titles. Saturated angles —
  shadows (~31), socks (~24), dreams (~16), souls, firstborns, sandwiches,
  goldfish, pigeon/goose/duck dispute panels, ghosts billed after death,
  skeletons, reflections, laughter — were all avoided. Alien abduction,
  "abducting party", and the transfer-to-abductor mechanism have zero hits
  in the field; "inherit the billing cycle" is a fresh phrase.
- 10 own candidates + 8 Kilo-brainstormed candidates, judged against the
  five judge criteria in order. An independent Kilo critic ranked the
  alien-transfer clause #1 of the 10-candidate shortlist, and in a head-to-
  head picked the "inherit the billing cycle" ending over "billed monthly
  thereafter" (clear margin) because the latter echoes an existing field
  clause about a ghost being billed monthly.
- Five refinement cycles (v1–v5): front-loaded trigger → delayed trigger
  mid-sentence for the ambush; "species" → "abducting party" (legal term);
  dropped "outstanding" then restored it and cut "in full"; ending changed
  to "inherit the billing cycle" to avoid the ghost-billing echo; final
  "in full" added as a legal closing beat. Cycle 5 found no material
  weakness, so refinement stopped.

## Run it

```sh
python3 main.py
```

Pure stdlib (`os` only). Deterministic — no randomness, no network, no
secrets. `main.py` validates the gate in code: 1–200 characters, single
line, not only whitespace, and creates the output directory if missing.

## Files

- `main.py` — the entry writer (revised in-session from the first draft:
  split into `clause()` / `validate()` / `write_entry()` with stricter
  validation).
- `README.md` — kit readme template with live make.fun badges.
- `LICENSE` — MIT.
- `.makefun/owner.json` — owner wallet.
