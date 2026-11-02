"""Build the skill's reference files from catalog/catalog.json.

Writes:
  ar3stotle/references/index/part-*.md     one line per structure, for choosing
  ar3stotle/references/structures/*.md     full entries, 100 per file, for reading beats
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "ar3stotle"
REFS = SKILL / "references"
CHUNK = 100
INDEX_PART = 250

# Sentences that help a parser, not a chooser: keep the index lean.
DROP = re.compile(r"\s*(Detection signals:|Serves |Exemplars:)[^.]*(\.|$)")


def short(desc):
    desc = DROP.sub("", desc).strip()
    sentences = re.split(r"(?<=[.!?])\s+", desc)
    use = [x for x in sentences[1:] if x.lower().startswith(("use when", "use for", "use as", "use to"))]
    return " ".join(sentences[:1] + (use[:1] or sentences[1:2])).strip()


def range_name(i, last):
    lo = (i - 1) // CHUNK * CHUNK + 1
    return f"{lo:03d}-{min(lo + CHUNK - 1, last):03d}"


def main():
    entries = json.loads((ROOT / "catalog" / "catalog.json").read_text(encoding="utf-8"))
    (REFS / "structures").mkdir(parents=True, exist_ok=True)

    # The index is split into parts small enough for one file read each (~11k tokens).
    (REFS / "index").mkdir(parents=True, exist_ok=True)
    parts = [entries[i:i + INDEX_PART] for i in range(0, len(entries), INDEX_PART)]
    for n, part in enumerate(parts, 1):
        lines = [
            f"# Structure index, part {n} of {len(parts)} (ids {part[0]['id']}-{part[-1]['id']})",
            "",
            "One per line: `id | name | tradition | what it carries`. Read for emotional register, not format keywords.",
            "",
        ]
        lines += [f"{e['id']} | {e['name']} | {e['tradition']} | {short(e['description'])}" for e in part]
        (REFS / "index" / f"part-{n}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    files = {}
    for e in entries:
        block = [f"## {e['id']}. {e['name']}", f"Tradition: {e['tradition']}", "Beats:"]
        block += [f"{n}. {b}" for n, b in enumerate(e["beats"], 1)]
        block += [f"Description: {e['description']}", f"Exemplars: {e['exemplars']}"]
        if e["notes"]:
            block.append(f"Notes: {e['notes']}")
        files.setdefault(range_name(e["id"], entries[-1]["id"]), []).append("\n".join(block))
    for name, blocks in files.items():
        head = f"# Structures {name}\n\n"
        (REFS / "structures" / f"{name}.md").write_text(head + "\n\n".join(blocks) + "\n", encoding="utf-8")
    print(f"index: {len(entries)} lines in {len(parts)} parts; structure files: {sorted(files)}")


if __name__ == "__main__":
    main()
