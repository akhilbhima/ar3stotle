"""Parse catalog/narrative-catalog.md into catalog/catalog.json.

The markdown file is the source of truth; everything in the skill is built from it.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "catalog" / "narrative-catalog.md"
OUT = ROOT / "catalog" / "catalog.json"

HEAD = re.compile(r"^GENRE (\d+): (.+)$")
FIELD = re.compile(r"^  ([A-Z][^:]{0,90}): ?(.*)$")
BEAT = re.compile(r"^    (\d+)\. (.+)$")


def parse(text):
    entries, cur, field, section = [], None, None, None
    for line in text.splitlines():
        if line.startswith("# ") and not line.startswith("# NGC Narrative Catalog"):
            section = line[2:].strip()
            continue
        if line.startswith("## Final Distribution"):
            break
        m = HEAD.match(line)
        if m:
            cur = {"id": int(m.group(1)), "name": m.group(2).strip(), "section": section,
                   "tradition": None, "beats": [], "description": "", "exemplars": "", "notes": ""}
            entries.append(cur)
            field = None
            continue
        if cur is None:
            continue
        b = BEAT.match(line)
        if b and field == "beats":
            cur["beats"].append(b.group(2).strip())
            continue
        f = FIELD.match(line)
        if f:
            key, val = f.group(1).strip().lower(), f.group(2).strip()
            if key.startswith("laws"):
                field = "beats"
            elif key.startswith("tradition"):
                field = "tradition"
                cur["tradition"] = val
            elif key in ("tradition", "description", "exemplars", "notes"):
                field = key
                cur[key] = val
            else:
                field = None
            continue
        if line.startswith("      ") and field in ("description", "exemplars", "notes"):
            cur[field] += " " + line.strip()
        elif line.startswith("      ") and field == "beats" and cur["beats"]:
            cur["beats"][-1] += " " + line.strip()
    return entries


def main():
    entries = parse(SRC.read_text(encoding="utf-8"))
    problems = [e["id"] for e in entries if not e["beats"] or not e["description"]]
    ids = [e["id"] for e in entries]
    if len(set(ids)) != len(ids):
        sys.exit("duplicate ids")
    OUT.write_text(json.dumps(entries, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(entries)} entries -> {OUT.name}; missing beats/description: {problems}")
    print("no tradition:", [e["id"] for e in entries if not e["tradition"]])


if __name__ == "__main__":
    main()
