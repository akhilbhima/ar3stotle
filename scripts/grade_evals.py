"""Grade one eval iteration: python3 scripts/grade_evals.py <workspace>/iteration-N

Checks each run's outputs/response.md and writes grading.json beside outputs/.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = {e["id"]: e["name"] for e in json.loads((ROOT / "catalog" / "catalog.json").read_text())}

BANNED = [
    r"\bit'?s not (just )?\w[^.]{0,40}, it'?s\b", r"\bnot just\b[^.]{0,40}\bbut\b", r"\bin a world where\b",
    r"\bthe truth is\b", r"\bhere'?s the thing\b", r"\bwhat if i told you\b", r"\bit'?s worth noting\b",
    r"\bat its core\b", r"\bmore than just\b", r"\bin today'?s fast-paced\b", r"\blet'?s dive in\b",
    r"\bbuckle up\b", r"\barguably\b", r"\bit could be said\b",
]

FACTS = {
    "funding-plea-email": ["Loomwork", "Halcyon", "41", "300", r"(six|6) weeks"],
    "rewrite-flat-linkedin": [r"(nine|9) years", "Deloitte", "senior manager", "Ana Ruiz", "2016", "Massa Mãe", "Porto", r"(3|third|3rd) (of )?February|February 3"],
    "wedding-toast": ["Priya", "Tom", "bike", "2019", "glass"],
}


def split(text):
    """Return (piece, signature) around the ⁂ signature, if any."""
    i = text.find("⁂")
    if i < 0:
        return text, ""
    head = text[:i].rstrip()
    head = re.sub(r"\n-{3,}\s*$", "", head)
    return head, text[i:]


def check(case, text):
    piece, sig = split(text)
    out = []
    m = re.search(r"Shaped with \*{0,2}(.+?)\*{0,2} \(#(\d+)", sig)
    out.append(("Response ends with a ⁂ signature naming a structure and its #id", bool(m),
                m.group(0) if m else "no signature found"))
    ok = bool(m) and int(m.group(2)) in CATALOG and CATALOG[int(m.group(2))].split(" (")[0].lower() in m.group(1).lower()
    out.append(("Named structure is a real catalog entry (id and name agree)", ok,
                f"#{m.group(2)} '{m.group(1)}' vs catalog '{CATALOG.get(int(m.group(2)))}'" if m else "n/a"))
    em = re.search(r"Emotion:\s*(.+)", sig)
    out.append(("Signature has an 'Emotion:' rationale line", bool(em), em.group(0)[:120] if em else "missing"))
    beats = re.search(r"Beats:\s*(.+)", sig)
    n = len(re.findall(r"\d\.", beats.group(1))) if beats else 0
    out.append(("Signature lists exactly three beats", n == 3, f"{n} beats"))
    hits = [p for p in BANNED if re.search(p, piece, re.I)]
    out.append(("Piece uses none of the banned voice phrases", not hits, ", ".join(hits) or "clean"))
    missing = [f for f in FACTS[case] if not re.search(f, piece, re.I)]
    out.append(("Piece keeps every required fact from the request", not missing, "missing: " + ", ".join(missing) if missing else "all present"))
    if case == "wedding-toast":
        words = len(re.findall(r"[A-Za-z']+", re.sub(r"\*\([^)]*\)\*", "", piece)))
        out.append(("Toast is about 2 minutes spoken (230-360 words)", 230 <= words <= 360, f"{words} words"))
    return out


def main():
    it = Path(sys.argv[1])
    for case_dir in sorted(p for p in it.iterdir() if p.is_dir()):
        for run in sorted(p for p in case_dir.iterdir() if p.is_dir()):
            resp = run / "outputs" / "response.md"
            if not resp.exists():
                continue
            results = check(case_dir.name, resp.read_text(encoding="utf-8"))
            exp = [{"text": t, "passed": p, "evidence": e} for t, p, e in results]
            passed = sum(p for _, p, _ in results)
            grading = {"expectations": exp, "summary": {"passed": passed, "failed": len(results) - passed,
                                                         "total": len(results), "pass_rate": round(passed / len(results), 2)}}
            (run / "grading.json").write_text(json.dumps(grading, ensure_ascii=False, indent=1))
            print(f"{case_dir.name}/{run.name}: {passed}/{len(results)}")


if __name__ == "__main__":
    main()
