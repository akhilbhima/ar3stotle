# ⁂ AR3STOTLE

Write anything on a real story structure, picked by the feeling you want to leave someone with.

AR3STOTLE is a free, open-source skill for Claude. It carries a catalog of **926 narrative structures from 10 traditions** (Japanese, Korean, Chinese, Indian, Persian-Arabic, West African, Indigenous Americas, Celtic-Norse, Latin American and the Western canon, plus 166 originals). When you ask Claude to write something, the skill reads what the piece should make your reader feel, picks the structure whose emotional register fits, shapes it into three beats, and then writes.

> Today's AI writing tools generate fluent text, but not narrative shape. The default voice of generative AI is the median of the English internet: capable, generic, structureless.
>
> The catalog is the bones; the model supplies the flesh.

The 3 in the name is the three beats.

## How it works

1. **Read the request.** What does it express, and what should the finished piece make the reader feel? Those are often different: a founder writing in panic may need the reader to feel steadiness.
2. **Choose by emotion first, format second.** Shortlist the structures whose register matches the feeling, then pick the one that also suits the format. A cold email asking for money from a broken place gets a Plea, not a sales template. Famous shapes like the Hero's Journey only win when they genuinely fit.
3. **Fit three beats.** Kishōtenketsu has four, Propp has thirty-one; every structure is compressed into three movements written for *your* people, claims and stakes.
4. **Write.** Each beat stops when it has a claim, evidence and one specific detail (the Just Enough Test). Voice rules strip out the tics that make AI prose sound like AI: "it's not X, it's Y", "in a world where", pitch-deck triplets.

Every piece ends with a small signature so you can see what shaped it and steer:

```
⁂ Shaped with **Plea (compressed)** (#770, Universal, NGC-original)
Emotion: dignity under pressure, desperation held in check.
Beats: 1. Their power to say no → 2. The ask → 3. What the money protects
```

Ask for "another structure", a different emotion, or name one yourself ("write it as a Kishōtenketsu").

## Install

**Claude (claude.ai or the desktop app):** download [`ar3stotle.skill`](dist/ar3stotle.skill), then open Settings → Capabilities → Skills and upload it.

**Claude Code:**

```bash
git clone https://github.com/akhilbhima/ar3stotle.git
cp -r ar3stotle/ar3stotle ~/.claude/skills/
```

Then just ask Claude to write something: an email, a toast, a post, a eulogy, a pitch. Saying "use ar3stotle" makes sure it kicks in.

## What's in here

| Path | What it is |
|---|---|
| `ar3stotle/` | The skill itself: `SKILL.md` plus its reference files |
| `catalog/narrative-catalog.md` | The catalog, the single source of truth (926 entries: tradition, beats, description, exemplars) |
| `catalog/catalog.json` | The same catalog as structured data, for your own tools |
| `scripts/parse_catalog.py` | Rebuilds `catalog.json` from the markdown |
| `scripts/build_skill.py` | Rebuilds the skill's reference files from `catalog.json` |
| `scripts/grade_evals.py` | Checks the skill's test runs |

To change or add a structure, edit `catalog/narrative-catalog.md`, then run:

```bash
python3 scripts/parse_catalog.py && python3 scripts/build_skill.py
```

## License

The skill and scripts are MIT. The catalog (`catalog/` and the generated `ar3stotle/references/`) is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): use it for anything, including commercial work, as long as you credit **AR3STOTLE by Akhil Bhima**.

Made by [Akhil Bhima](https://akhilbhima.com).
