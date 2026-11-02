---
name: ar3stotle
description: Write anything on a real narrative structure picked by emotion from 926 storytelling forms across 10 traditions (Kishōtenketsu, Noh, Propp, Hero's Journey, the Plea, the Quiet Pivot and hundreds more). Use this skill whenever the user asks to write, draft or rewrite something meant to move a reader (an email, post, essay, speech, story, script, pitch, apology, eulogy, letter, landing page, thread) or says "ar3stotle", "write it as a story", "give this a narrative", "which story structure fits", or "make this land". Also use it to rewrite flat text into something with shape, even if the user never mentions structure.
---

# ⁂ AR3STOTLE

Most AI writing is fluent but shapeless: the median of the internet, with no arc. AR3STOTLE fixes the shape first. It reads what the writing should make someone *feel*, picks a structure from a catalog of 926 narrative forms whose emotional register matches, fits that structure to three beats, and only then writes.

The catalog is the bones; you supply the flesh. The 3 in the name is the three beats.

## The method

Work through these four steps in order. Steps 1-3 are thinking, not output: keep them to yourself unless the user asks to see the brief.

### 1. Read the request

Decide the **mode**. If the user handed you existing text to improve (roughly 80+ words, four or more sentences, or several paragraphs), it is a **rewrite**. Otherwise it is a **generate**.

In a rewrite, the facts are sacred and the sentences are not. Keep every name, number, date and claim, but write the piece fresh on the new structure, in the author's own register (first person stays first person, a LinkedIn post stays a LinkedIn post). The user asked for a rewrite because the original sentences were the problem, so reusing them ("I have decided to leave my role as…") carries the flatness straight through.

Then pull out:

- **Emotional signal**: what the request itself expresses (frustrated, proud, grieving, rushed).
- **Emotional target**: what the finished piece should make the reader feel, and how strongly. This is often different from the signal, and it drives everything after. A founder writing in panic may need the reader to feel steadiness.
- **Facts**: named people, organisations, products and things; claims that must survive; explicit must-include and must-avoid rules.
- **Intent**: the purpose, the specific domain ("nonprofit fundraising", not "writing") and who reads it.
- **Format and length**: a noun phrase ("cold email", "wedding toast", "LinkedIn post", "memoir excerpt") and a word count from the format's conventions when none is given (tweet ~50, email ~200, landing page ~300, blog post ~800).

If something essential is missing and can't be inferred, ask one short question. Otherwise infer and keep going: the system asks only what it can't infer.

### 2. Choose the structure, emotion first

Read all four index files: `references/index/part-1.md` to `part-4.md`. Each line is `id | name | tradition | what it carries`.

1. **Emotion first.** Hold the emotional target in mind and shortlist 5-10 structures whose described register matches it. The description is the strongest signal; read it for feeling, not for format words.
2. **Then format.** From that shortlist, pick the one that also serves the intent and the format.
3. **Read the full entry.** Open the matching file in `references/structures/` (id 412 is in `401-500.md`, id 926 is in `901-926.md`) for its beats, description and exemplars.

Picking on format alone is the failure mode. A cold email asking for funding because the company is struggling should not get a generic sales structure just because it is an email; its cargo is desperation and dignity, so look for a plea, a confession, a last stand. Format is the wrapper; emotion is the cargo.

Famous shapes like the Hero's Journey or an Origin Story are over-represented in training data. Use one only when its description genuinely matches this emotional weight.

Write a one-line **rationale that starts with the emotion**: "Emotion: dignity, desperation. The Plea holds the asker upright while admitting the stakes." If your rationale starts with the format ("this fits an email"), you picked on format. Go back to step 2.1.

**Fit exactly three beats.** Whatever the source structure's beat count (Kishōtenketsu has 4, Propp has 31), compress or group its beats into three movements written for *this* request: its people, its claims, its stakes. Three is the smallest unit of a story: a setup, a shift, a resolution. Never copy the catalog's beat text verbatim.

### 3. Build the brief

- **Persona**: a specific writer, not "a writer". Name the role ("senior copywriter for nonprofit fundraising appeals"), 3-5 relevant skills and 2-4 voice traits. If the user gave their own voice, brand rules or a sample of their writing, that voice wins over the persona.
- **Must include**: every entity and claim from step 1.
- **Must avoid**: anything the user ruled out, plus phrases that would break the tone.
- **Tone**: one sentence on how the piece should feel, from the emotional target.
- **Length**: the word count from step 1.
- **Structural elements**: concrete markdown patterns, not abstract names. Use `# Title` and `## Section` for long prose; `**[HOOK - 0:00-0:10]**` labels and `*(stage directions)*` for scripts, podcasts and ad reads; nothing at all for a tweet or a short email.

### 4. Write

Write the piece as the persona, moving through the three beats in order.

**The Just Enough Test, per beat.** A beat is done when it has a claim (what is true), evidence (a fact, story or observation that shows it) and one specific detail (a concrete image, number or name). Without all three the beat is thin; with much more it is bloated. Once all three are there, move to the next beat.

**Voice rules.** These keep the output human and override any tendency from the persona or structure:

- No antithesis framing: "It's not X, it's Y", "Not just X, but Y", "Less X, more Y". State the positive claim directly. Contrast is fine only when the contrast *is* the idea, and at most once.
- No LLM-isms: "In a world where", "The truth is", "Here's the thing", "What if I told you", "It's worth noting", "At its core", "More than just", "In today's fast-paced", "Let's dive in", "Buckle up".
- No empty hedges ("arguably", "perhaps", "it could be said") and no em-dash sandwiches that smuggle in a contrast ("X — not Y — is Z").
- No pitch-deck rhythm: no sermons about "organizations that…", no triple outcomes like "close faster, retain better, grow smarter". Write like a person with a story.
- Keep people as people. Never swap a named person for a product or brand, and never make a tool the subject of a sentence about someone's choices or feelings.
- Prefer declarative sentences and specific nouns and verbs. If a sentence is as strong without its "not X" half, cut that half.

No preamble. Output the content itself, formatted with the structural elements from the brief.

## What the user sees

First the piece. Then a short signature so the user knows what shaped it and can steer:

```
---
⁂ Shaped with **<structure name>** (#<id>, <tradition>)
Emotion: <the rationale line>
Beats: 1. <beat> → 2. <beat> → 3. <beat>
```

Then one line offering the next move, in your own words: they can ask for a different structure, a different emotion, or a shorter or longer cut.

When asked for "another structure", go back to your step 2 shortlist and take the next best fit; don't restart from scratch. When the user names a structure ("write it as a Kishōtenketsu"), look it up and use it; still fit three beats and still write the emotion line.

If the user only wants advice ("which structure fits my eulogy?"), skip writing: give your top three from the shortlist, each with its emotion line and its three fitted beats, best first.

## Edits after the first draft

For a small edit ("make the second paragraph shorter", "warmer ending"), change only what was asked and keep the structure. For a big change of feeling ("make it angrier", "this should feel hopeful"), redo step 2 with the new emotional target, because a different feeling usually needs a different shape.
