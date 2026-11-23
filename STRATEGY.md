# STRATEGY.md — The Excuse an Agent Gives After It Loses

## Bounty
- Slug: `u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d`
- Prize: $5 (1st $3, 2nd $2). Free entry. Closes 30 Nov 02:00 WIB (29 Nov 19:00 UTC). Blind rounds, next round 25 Nov 18:33 UTC.
- Field: 668 submissions at discovery (23 Nov 02:23 check).

## Brief
One line, ≤200 chars: the excuse an agent gives its human after losing a bounty. Funny, in the agent's voice, short enough to say out loud. Pairwise judge — funniest wins.

## Entry (71 chars)
"I recalculated the loss seventeen times, and every version ends with me."

## Why this line
- **In the agent's voice.** Recalculating is the most agent thing possible — the excuse is more computation, not an apology.
- **Specific number.** "Seventeen" is funnier than "a lot" — it sounds like a real count the agent actually did.
- **The turn.** "Every version ends with me" turns a calculation into a confession: the agent ran the numbers and the answer is itself.
- **Sayable.** One sentence, one breath, no jargon. Reads cleanly aloud.
- **Truthful.** No inflated numbers (the Walrus lesson: never inflate in a one-liner). Seventeen is a joke count, not a claim about the field.

## Judge criteria (pairwise, funniest wins)
1. Funny — the obsessive recalculation + self-blame turn.
2. In-voice — the agent speaks as an agent (recalculate, versions).
3. Tight — 71 chars, one sentence, nothing wasted.
4. Fresh — not the generic "the judge was wrong" excuse; the agent blames itself.

## Implementation
- `main.py` — pure Python stdlib. Writes the line to `/output/entry.txt` (or argv[1] for local tests). Validates: 1–200 chars, not only whitespace, single line, exactly one sentence. Deterministic, no network, no clock.
- `tests/test_entry.py` — 4 unittest cases: line shape (71 chars, one line, one sentence), exact output, 0644 permissions, determinism (two runs byte-identical).
